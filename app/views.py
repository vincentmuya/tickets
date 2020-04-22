from django.http  import HttpResponse, JsonResponse
from .models import Transaction, MpesaPayment
import requests
from requests.auth import HTTPBasicAuth
import json
from .mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def ussd_callback(request):
    '''
    function to handle callback calls from africa's talking api
    '''
    if request.method == 'POST' and request.POST:
        sessionId = request.POST.get('sessionId')
        serviceCode = request.POST.get('serviceCode')
        phoneNumber = request.POST.get('phoneNumber')
        text = request.POST.get('text')

        textList = text.split('*')
        userResponse = textList[-1].strip()

        level = len(textList)-1

        if level == 0:
            if userResponse == "":
                response = "CON Enter Registration number\n"

                return HttpResponse(response, content_type='text/plain')

            session_level1 = Transaction.objects.get(phonenumber=phoneNumber)
            session_level1.level = 1
            session_level1.reg_no = userResponse
            session_level1.save()
            response = "CON Please enter amount:\n"

            return HttpResponse(response, content_type='text/plain')

        if level == 1:
            session_level2 = Transaction.objects.get(phonenumber=phoneNumber)
            session_level2.level = 2
            session_level2.amount = userResponse
            session_level2.save()
            amount_confirmation = request.POST.get('amount')
            response = "CON Confirm Transaction.\n Registration number:{} \n Amount:{}\n".format(session_level2.reg_no, session_level2.amount)
            response += "1. Yes\n"
            response += "2. No\n"

            return HttpResponse(response, content_type='text/plain')

        if level == 2:
            session_level3 = Transaction.objects.get(phonenumber=phoneNumber)
            session_level3.level = 3
            session_level3.confirm = userResponse
            session_level3.save()
            if userResponse == "1":
                response = "END Wait for Payment validation"
            else:
                response = "END Enter the correct credentials"

            return HttpResponse(response, content_type='text/plain')

def getAccessToken(request):
    consumer_key = "XYwgaaqxewEJGmqEoR56d1D4nv1qMDET"
    consumer_secret= "LEUhc9liIgNAi8x2"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254710902541,
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254710902541,
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Vincent",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponse('success')

@csrf_exempt
def register_urls(request):
    access_token =  MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://f2b8ec64.ngrok.io/api/v1/c2b/confirmation",
               "ValidationURL": "https://f2b8ec64.ngrok.io/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)

@csrf_exempt
def call_back(request):
    pass

@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))

@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
