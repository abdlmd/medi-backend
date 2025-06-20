from rest_framework import serializers
from django.contrib.auth import get_user_model
from aid.models import AidRequest
class SimpleCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=["id","username","first_name","last_name"]
class AidRequestSerializer(serializers.ModelSerializer):
    created_by=SimpleCreatorSerializer(read_only=True)
    fulfilled_by=SimpleCreatorSerializer(read_only=True)
    
    class Meta:
        model=AidRequest
        fields=["id","title","description","types","created_by","created_at","updated_at","fulfilled_status","fulfilled_by"]
        read_only_fields = ["created_by", "created_at", "updated_at", "fulfilled_by"]