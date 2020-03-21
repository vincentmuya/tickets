from django.shortcuts import render, get_object_or_404, redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.db import transaction
from .forms import UserForm,ProfileForm


# Create your views here.
@login_required(login_url='/accounts/login')
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
