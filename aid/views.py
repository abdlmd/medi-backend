from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import AidRequestSerializer
from .models import AidRequest
# Create your views here.

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_aid_request(request):
    serializer=AidRequestSerializer(data=request.data)
    user=request.user
    if serializer.is_valid():
        serializer.save(created_by=user)
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_aid_requests(request):
    aid_requests=AidRequest.objects.all()
    serializer=AidRequestSerializer(aid_requests,many=True)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def volunteer_for_request(request,pk):
    user=request.user
    aid_request=AidRequest.objects.get(id=pk)
    aid_request.fulfilled_status = True
    aid_request.fulfilled_by = user
    aid_request.save()
    serializer=AidRequestSerializer(aid_request)
  
    
    return Response(serializer.data)

    
    



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_my_posted_request(request):
    aid_requests=AidRequest.objects.filter(created_by=request.user)
    serializer=AidRequestSerializer(aid_requests,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_my_volunteered_request(request):
    
    aid_requests=AidRequest.objects.filter(fulfilled_by=request.user)
    serializer=AidRequestSerializer(aid_requests,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_aid_by_type(request,type_name):
    aid_requests=AidRequest.objects.filter(types=type_name)
    serializer = AidRequestSerializer(aid_requests,many=True)
    return Response(serializer.data)
 

