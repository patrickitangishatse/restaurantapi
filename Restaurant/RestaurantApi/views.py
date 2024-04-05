from django.shortcuts import render
from .models import Restaurant, RestaurantOwner
from .Serializers import RestaurantSerializer, RestaurantOwnerSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend



# Create and Get all Restaurants

class CreateRestaurant(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['address', 'owner']
    search_fields=['name' , 'address', 'owner'] 
    


# Get,Update and Delete Specific Restaurant 
class RestaurantDetails(RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'  



# Create and Get all Restaurant Owners
class CreateOwner(ListCreateAPIView):
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantOwnerSerializer


# Get,Update and Delete Specific Restaurant Owner
class OwnerDetails(RetrieveUpdateDestroyAPIView):
    queryset = RestaurantOwner.objects.all()
    serializer_class = RestaurantOwnerSerializer
    lookup_field = 'id'

