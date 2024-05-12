from django.forms import ModelForm
from django import forms
from .models import *


# class UserUpdateForm(ModelForm):
#     class Meta:
#         models = User
#         fields = ['username', 'password', 'email']


# class UserProfileForm(ModelForm):
#     class Meta:
#         models = Profile
#         fields = ['user_mobile', 'designation', 'user_university', 'user_description', 'user_profile_pic', 'user_profile_cover']


class ProjectUploadForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class TemplateUploadForm(ModelForm):
    class Meta:
        model = Templates
        fields = '__all__'
