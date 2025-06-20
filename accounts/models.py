from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLES=(("patient","patient"),("volunteer","volunteer"),("doctor","doctor"),("pharmacy","pharmacy"))
    role=models.CharField(choices=ROLES,max_length=20)
    phoneNumber=models.TextField(blank=False,null=False,max_length=13)
    profilePicture=models.ImageField(blank=True,null=True,upload_to="profile_img")
    approval=models.BooleanField(default=False,null=False,blank=False)

    def __str__(self):
        return self.username
    
