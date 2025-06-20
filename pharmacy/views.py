from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .serializers import MedicineSerializer
from .models import Medicine

# Create your views here.
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_medicine(request):
    serializer=MedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(pharmacy=request.user)
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_all_medicines(request):
    medicines=Medicine.objects.all()
    serializer=MedicineSerializer(medicines,many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_my_medicines(request):
    medicines=Medicine.objects.filter(pharmacy=request.user)
    serializer=MedicineSerializer(medicines,many=True)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_medicine(request,pk):
    medicine=Medicine.objects.get(id=pk)
    medicine.price=request.data.get("price")
    medicine.quantity=request.data.get("quantity")
    medicine.save()
    serializer=MedicineSerializer(medicine)
    return Response(serializer.data)

@api_view(["GET"])
def filter_medicine(request,category_request):
    medicines=Medicine.objects.filter(category=category_request)
    serializer=MedicineSerializer(medicines,many=True)
    return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_medicine(request,pk):
    medicine=Medicine.objects.get(id=pk)
    medicine.delete()
    return Response("Deleted Succesfully")



