from rest_framework import serializers
from django.contrib.auth import get_user_model
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=["id","username","first_name","last_name","email","phoneNumber","role","profilePicture","password","approval"]

        extra_kwargs={'password':{'write_only':True}}
    def create(self,validated_data):
        email=validated_data["email"]
        username=validated_data["username"]
        first_name=validated_data["first_name"]
        last_name=validated_data["last_name"]
        phoneNumber=validated_data["phoneNumber"]
        role=validated_data["role"]
        profilePicture=validated_data["profilePicture"]
        password=validated_data["password"]
        approval=validated_data["approval"]
        user=get_user_model()
        new_user=user.objects.create(email=email,username=username,first_name=first_name,last_name=last_name,phoneNumber  =phoneNumber,role=role,profilePicture=profilePicture,approval=approval    )
        new_user.set_password(password)
        new_user.save()
        return new_user