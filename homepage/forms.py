from django.forms import ModelForm

from .models import *
class UserFrom(ModelForm):
    class Meta:
        models = User
        fields = '__all__'