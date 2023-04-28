from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal


# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    info = models.CharField(max_length=255,null=True, blank=True)
    location = models.CharField(max_length=255,null=True,blank=True)
    bio = models.TextField(null=True, blank=True)
    social_github = models.CharField(max_length=255,null=True,blank=True)
    social_telegram = models.CharField(max_length=255, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()



    def __str__(self) -> str:
        return self.name


class Skill(models.Model):
    user = models.ForeignKey(Profil, on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    print(name)



    def __str__(self) -> str:
        return self.name

def create_profile(sender, instance, created, **kwargs):
    print(f"sender: {sender}\n instance: {instance}\n created: {created}\n")


Signal.connect(post_save, create_profile)