from django.contrib import admin
from .models import UserProfile, Project, Achievement, Skill

# Register your models here.
admin.site.register([UserProfile, Project, Achievement, Skill])