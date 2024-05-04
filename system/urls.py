"""
URL configuration for system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homepage import views as a_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', a_views.home, name='home'),
    path('signUp/', a_views.signUp, name='signUp'),
    # path('feed/', a_views.feed, name='feed'),
    path('ideasHub/', a_views.ideasHub, name='ideasHub'),
    path('profile/', a_views.profile, name='profile'),
    path('templatesLib/', a_views.templatesLib, name='templatesLib'),
    path('AccStatus/', a_views.AccStatus, name='AccStatus'),
    path('activityLog/', a_views.activityLog, name='activityLog'),

    path('logIn/', a_views.loginUser, name='logIn'),
    path('logout', a_views.logOutUser, name='logout'),
    
    path('moderation/', a_views.moderation, name='moderation'),
    path('orderAndPayments/', a_views.orderAndPayments, name='orderAndPayments'),
    path('settings/', a_views.settings, name='settings'),
    path('updateProfile/', a_views.profileUpdate, name='updateProfile'),

    path('uploadProject/', a_views.uploadProject, name='uploadProject'),
    path('cartTemp/', a_views.cartTemp, name='cartTemp'),
    path('likedProject/', a_views.likedProject, name='likedProject'),
    path('messenger/', a_views.messenger, name='messenger'),
    path('searchPeople/', a_views.searchPeople, name='searchPeople'),
    path('someonesProfile/', a_views.someonesProfile, name='someonesProfile'),

    path('user_Delete/', a_views.delete_User, name='user_Delete'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)