from django.shortcuts import render, redirect
from .forms import *
from .models import Profile, Templates
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, template_name='Home.html')


def signUp(request):
    if request.method =='POST':

        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        uniname = request.POST.get('uniname')
        designation = request.POST.get('designation')
        description = request.POST.get('description')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        profile = Profile.objects.create(user = user,user_mobile=phone,user_university =uniname,designation=designation,user_description = description)
        profile.save() 
        return redirect('/')
             
    
    return render(request, template_name='signup.html')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return redirect('/')  
        return render(request,'login.html')
    
def logOutUser(request):
    auth.logout(request)
    return redirect('/')
    
# feed removed
# def feed(request):
    # return render(request, template_name='feed.html')


def ideasHub(request):
    return render(request, template_name='ideas hub.html')


def profile(request):
    return render(request, template_name='profile.html')


def templatesLib(request):
    templates = Templates.objects.all()
    context = {
        'templates': templates,
    }

    return render(request, template_name='templates library page.html')


def AccStatus(request):
    return render(request, template_name='account status.html')


def activityLog(request):
    return render(request, template_name='activity log.html')


def moderation(request):
    return render(request, template_name='moderation.html')


def orderAndPayments(request):
    return render(request, template_name='orders and payments.html')


def settings(request):
    return render(request, template_name='settings.html')


def updateProfile(request):
    return render(request, template_name='Update profile.html')


def uploadProject(request):
    return render(request, template_name='uploadproject.html')


def cartTemp(request):
    return render(request, template_name='cartfortemplates.html')


def likedProject(request):
    return render(request, template_name='liked project.html')


def messenger(request):
    return render(request, template_name='messenger.html')


def searchPeople(request):
    return render(request, template_name='searchpeople.html')


def someonesProfile(request):
    return render(request, template_name='someones profile.html')



