from rest_framework import serializers
from consults.models import ConsultRequest
from django.contrib.auth import get_user_model
class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=["id","username","first_name","last_name"]
class ConsultRequestSerializer(serializers.ModelSerializer):
    patient=SimpleUserSerializer(read_only=True)
    doctor=SimpleUserSerializer(read_only=True)
    class Meta:
        model=ConsultRequest
        fields=["id","symptoms","description","status","created_at","patient","doctor"]
        read_only_fields=["created_at","patient","doctor"]