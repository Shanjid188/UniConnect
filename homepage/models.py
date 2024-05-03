from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator




# Create your models here.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # user_name = models.CharField(max_length=200)
    # user_email = models.EmailField(max_length=200)
    # user_password = models.CharField(max_length=50)

    user_mobile = models.CharField(max_length=11, null=True, blank=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    user_university = models.CharField(max_length=100, blank=True, null=True)
    user_description = models.TextField(blank=True, null=True)
    user_profile_pic = models.ImageField(upload_to='upload',null=True,blank=True)
    user_profile_cover = models.ImageField(upload_to='upload', null=True, blank=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    project_title = models.CharField(max_length=200)
    project_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.project_title


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    achievement_title = models.CharField(max_length=200)
    achievement_description = models.TextField(blank=True, null=True)
    achievement_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.achievement_title


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    skill_title = models.CharField(max_length=200)
    skill_level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.skill_title