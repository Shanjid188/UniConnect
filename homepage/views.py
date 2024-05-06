from django.shortcuts import render, redirect
from .forms import *
from .models import Profile, Templates
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .updateForm import UserUpdateForm , UserProfileForm

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


def delete_User(request):
    delUser = User.objects.get(username = request.user.username)

    if request.method == 'POST':
        delUser.delete()
        return redirect('home')
    return render(request, 'deleteUser.html')


def profileUpdate(request):
    # formU = UserCForm()
    # formP = UserProfileForm()
    user = User.objects.get(username = request.user.username)
    print(user)

    pro = Profile.objects.get( user = user)
    print(pro)
    formU = UserUpdateForm(instance = user)
    formP = UserProfileForm(instance = pro)
    if request.method == 'POST':

        # username = request.POST.get('username')
        # phone = request.POST.get('phone')
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # uniname = request.POST.get('uniname')
        # designation = request.POST.get('designation')
        # description = request.POST.get('description')
        # picture = request.POST.get('profilePic')
        # cover = request.POST.get('coverPic')


        formU = UserUpdateForm(request.POST, request.FILES, instance=user)
        formP = UserProfileForm(request.POST, request.FILES, instance=pro)

        # user.update(username=username, email=email, password=password)
        # pro.update(user=user, user_mobile=phone, user_university=uniname, designation=designation,
        #            user_description = description, user_profile_pic=picture, user_profile_cover=cover)
        #
        # user.save()
        # pro.save()

        if formP.is_valid():
            formP.save()
        if formU.is_valid():
            formU.save()
        # context = {
        #     'title':'Successfull',
        #     'm1': request.user.username,
        #     'm2':'your profile Update Successfull',
        #     'url':'profile',
        #     }
        return render(request, 'profile.html') #, context)

    context = {
        'formP':formP,
        'formU':formU
    }

    return render(request, 'Update profile.html', context)


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
    return render(request, template_name='activityLog.html')


def moderation(request):
    return render(request, template_name='moderation.html')


def orderAndPayments(request):
    return render(request, template_name='orders and payments.html')


def settings(request):
    return render(request, template_name='settings.html')



def uploadProject(request):
    formUP = ProjectUploadForm()
    if request.method == 'POST':
        formUP = ProjectUploadForm(request.POST)
        if formUP.is_valid():
            formUP.save()
            return redirect('profile')

    context = {
        'formUP': formUP,
    }
    return render(request, template_name='uploadproject.html', context=context)


def cartTemp(request):
    return render(request, template_name='cartfortemplates.html')


def save(request):
    return render(request, template_name='save.html')


def messenger(request):
    return render(request, template_name='messenger.html')


def searchPeople(request):
    return render(request, template_name='searchpeople.html')


def someonesProfile(request):
    return render(request, template_name='someones profile.html')


# def notLoggedIdeasHub(request):
#     return render(request, template_name='notloggedIH.html')


def notLoggedTemplatesLibrary(request):
    return render(request, template_name='notloggedTL.html')


def aboutUser(request):
    return render(request, template_name='about.html')


def notLoggedIdeasHub(request):
    ideas = Project.objects.all()
    idea = {
        "ideas": ideas,
    }
    return render(request, 'notloggedIH.html', context=idea)
