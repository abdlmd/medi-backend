from django.db import models
from django.conf import settings

# Create your models here.
class ConsultRequest(models.Model):
    status_choices=(("PENDING","PENDING"),("CONFIRMED","CONFIRMED"))
    symptoms=models.TextField(null=False,blank=False,max_length=25)
    description=models.TextField(null=True,blank=True,max_length=300)
    status=models.CharField(choices=status_choices,max_length=30,default="PENDING")
    created_at=models.DateTimeField(auto_now_add=True)
    patient=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="consultancy_requester")
    doctor=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True,related_name="consults_received")


