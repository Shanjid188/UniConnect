from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, template_name='Home.html')


def signUp(request):
    return render(request, template_name='signUp.html')


def feed(request):
    return render(request, template_name='feed.html')


def ideasHub(request):
    return render(request, template_name='ideasHub.html')


def profile(request):
    return render(request, template_name='profile.html')


def templatesLib(request):
    return render(request, template_name='templatesLib.html')
