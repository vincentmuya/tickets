from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Transaction(models.Model):
    reg_no = models.CharField(max_length=30, null=True) # Registration Number
    amount = models.CharField(max_length=60, null=True) # Amount
    confirm= models.IntegerField(null=True)
    phonenumber= models.CharField(max_length=60)
    level = models.IntegerField(null=True)

    def save_user(self):
        self.save()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
# M-pesa Payment models
class MpesaCalls(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = "Mpesa Call Back"
        verbose_name_plural = "Mpesa Call Backs"

class MpesaCallBacks(BaseModel):
    ip_address = models.TextField()
    caller = models.TextField()
    conversation_id = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = "Mpesa Call Back"
        verbose_name_plural = "Mpesa Call Backs"

class MpesaPayment(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    type = models.TextField()
    reference = models.TextField()
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.TextField()
    organization_balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Mpesa Pyament"
        verbose_name_plural = "Mpesa Payments"

    def __str__(self):
        return self.first_name

class Payment(models.Model):
    reg_no = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    phone_number= models.CharField(max_length=25,null=True)

class session_levels(models.Model):
	session_id = models.CharField(max_length=25,primary_key=True)
	phone_number= models.CharField(max_length=25,null=True)
	level = models.IntegerField(null=True)
