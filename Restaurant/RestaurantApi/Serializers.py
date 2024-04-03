from .models import Restaurant, RestaurantOwner
from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name', 'cuisine_type', 'address', 'phone','rating', 'owner']


class RestaurantOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantOwner
        fields = ['id','FirstName', 'LastName', 'Gender','PhoneNumber','Nationality']

