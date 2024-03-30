from django.contrib import admin
from .models import User, Project, Achievement, Skill

# Register your models here.
admin.site.register([User,Project,Achievement,Skill])