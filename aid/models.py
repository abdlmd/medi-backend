from django.db import models
from django.conf import settings

# Create your models here.

class AidRequest(models.Model):
    TYPES=(("FOOD","FOOD"),("MEDICINE","MEDICINE"),("TRANSPORT","TRANSPORT"))
    title=models.TextField(null=False,blank=False)
    description=models.TextField(null=False,blank=False)
    types=models.CharField(choices=TYPES,null=False,blank=False,max_length=20)
    created_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="requests_created",null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    fulfilled_status=models.BooleanField(default=False)
    fulfilled_by=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name="requests_fulfilled")


