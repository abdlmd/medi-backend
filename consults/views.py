from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import ConsultRequestSerializer
from .models import ConsultRequest
# Create your views here.
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_consult_request(request):
    serializer=ConsultRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(patient=request.user)
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_all_consult_requests(request):
    all_consult_requests=ConsultRequest.objects.all()
    serializer=ConsultRequestSerializer(all_consult_requests,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_my_volunteered_consult_requests(request):
    all_volunteered=ConsultRequest.objects.filter(doctor=request.user)
    serializer=ConsultRequestSerializer(all_volunteered,many=True)
    return Response(serializer.data)



@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_my_consult_requests(request):
    my_consult_requests=ConsultRequest.objects.filter(patient=request.user)
    serializer=ConsultRequestSerializer(my_consult_requests,many=True)
    return Response(serializer.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_pending_requests(request):
    pending_requests=ConsultRequest.objects.filter(status="PENDING")
    serializer=ConsultRequestSerializer(pending_requests,many=True)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def confirm_consult_request(request,pk):
    consult_request=ConsultRequest.objects.get(id=pk)
    consult_request.doctor=request.user
    consult_request.status="CONFIRMED"
    consult_request.save()
    serializer=ConsultRequestSerializer(consult_request)
    return Response(serializer.data)
