from django import forms
from .models import User,Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone_number', 'profile_image',)
        exclude = ['first_name', 'last_name']
        widges = {
        }
