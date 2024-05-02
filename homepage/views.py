from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, template_name='Home.html')


def signUp(request):
    return render(request, template_name='sign up.html')

# feed removed
# def feed(request):
    # return render(request, template_name='feed.html')


def ideasHub(request):
    return render(request, template_name='ideas hub.html')


def profile(request):
    return render(request, template_name='profile.html')


def templatesLib(request):
    return render(request, template_name='templates library page.html')


def AccStatus(request):
    return render(request, template_name='account status.html')


def activityLog(request):
    return render(request, template_name='activity log.html')


def logIn(request):
    return render(request, template_name='log in.html')


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

