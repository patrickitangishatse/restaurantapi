from django.shortcuts import render
from .models import Restaurant, RestaurantOwner
from .Serializers import RestaurantSerializer, RestaurantOwnerSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView



# Create and Get all Restaurants

class RestaurantListCreate(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


# Get,Update and Delete Specific Restaurant 
class RestaurantRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'  



# Create and Get all Restaurant Owners
class RestaurantOwnerListCreate(ListCreateAPIView):
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantOwnerSerializer


# Get,Update and Delete Specific Restaurant Owner

class RestaurantOwnerRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantOwnerSerializer
    lookup_field = 'id'