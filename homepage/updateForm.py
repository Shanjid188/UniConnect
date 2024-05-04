from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']


class UserProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user_mobile', 'designation', 'user_university', 'user_description', 'user_profile_pic', 'user_profile_cover']
