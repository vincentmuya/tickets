from django.shortcuts import render, get_object_or_404, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db import transaction
from .forms import UserForm,ProfileForm
import requests
from requests.auth import HTTPBasicAuth
import json


# Create your views here.
def getAccessToken(request):
    consumer_key = "rC5JYdE2Kf0ivU6C0BHyG0Cp0PGi9rIZ"
    consumer_secret= "Cb1ZOEx9Qv8VOvXg"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    testing = "Hello World"
    context = {"validated_mpesa_access_token":validated_mpesa_access_token, "testing":testing}
    # return HttpResponse(validated_mpesa_access_token)
    return render(request, 'accesstoken.html',context )

def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login')
def profile(request, username):
    profile = Profile.objects.filter(user_id=request.user.id)
    return render(request, 'profile.html')

@login_required
@transaction.atomic
def update_profile(request, user_id):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
