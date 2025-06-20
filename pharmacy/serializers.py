from rest_framework import serializers
from pharmacy.models import Medicine
from django.contrib.auth import get_user_model
class SimplePharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=["id","username","first_name","last_name"]
    

class MedicineSerializer(serializers.ModelSerializer):
    pharmacy=SimplePharmacySerializer(read_only=True)
    class Meta:
        model = Medicine
        fields=["id","name","manufacturer","category","price","quantity","pharmacy","created_at","updated_at"]
        read_only_fields=["pharmacy","created_at","updated_at"]