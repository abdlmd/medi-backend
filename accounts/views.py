from django.shortcuts import render
from .serializers import UserRegistrationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes
# Create your views here.
@api_view(["POST"])
@parser_classes([MultiPartParser,FormParser])
def register_user(request):
     data=request.data.copy()
     role=data.get("role")
     if role =="patient":
         data["approval"]=True
     else:
         data["approval"]=True


     serializer=UserRegistrationSerializer(data=data)
    
     if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view_profile(request):
    user=request.user
    serializer=UserRegistrationSerializer(user)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_user_profile(request):
    user=request.user
    serializer = UserRegistrationSerializer(user,data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

   


