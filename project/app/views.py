from django.shortcuts import render, get_object_or_404, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    return render(request, 'index.html')
