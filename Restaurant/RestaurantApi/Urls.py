from django.urls import path
from .views import CreateRestaurant, RestaurantDetails, CreateOwner, OwnerDetails




urlpatterns = [
    path('restaurants/', CreateRestaurant.as_view(), name='Create-restaurant'),
    path('restaurants/<int:id>/', RestaurantDetails.as_view(), name='Details-restaurant'),
    path('owners/', CreateOwner.as_view(), name='register-owner'),
    path('owners/<int:id>/', OwnerDetails.as_view(), name='Detail-owner'),
]