from django.contrib import admin
from .models import MpesaPayment, Transaction
# Register your models here.
admin.site.register(MpesaPayment)
admin.site.register(Transaction)