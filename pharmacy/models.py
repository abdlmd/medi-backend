from django.db import models
from django.conf import settings
# Create your models here.
class Medicine(models.Model):
    categories=(("ANTIBIOTICS","ANTIBIOTICS"),("COUGH_MEDICINE","COUGH_MEDICINE"),("PAINKILLER","PAINKILLER"))
    name=models.TextField(null=False,blank=False,max_length=255)
    manufacturer=models.TextField(null=False,blank=False,max_length=255)
    category=models.CharField(choices=categories,null=True,blank=True,max_length=50)
    price=models.FloatField(null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    pharmacy=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="available_at_pharmacy")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
