from django.contrib import admin
from .models import Profile, Project, Achievement, Skill, Templates

# Register your models here.
admin.site.register([Profile, Project, Achievement, Skill, Templates])