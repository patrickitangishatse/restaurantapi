from django.urls import path
from .views import RestaurantListCreate, RestaurantRetrieveUpdateDestroy, RestaurantOwnerListCreate, RestaurantOwnerRetrieveUpdateDestroy




urlpatterns = [
    path('restaurants/', RestaurantListCreate.as_view(), name='restaurant-list-create'),
    path('restaurants/<int:id>/', RestaurantRetrieveUpdateDestroy.as_view(), name='restaurant-retrieve-update-destroy'),
    path('restaurant-owners/', RestaurantOwnerListCreate.as_view(), name='restaurant-owner-list-create'),
    path('restaurant-owners/<int:id>/', RestaurantOwnerRetrieveUpdateDestroy.as_view(), name='restaurant-owner-retrieve-update-destroy'),
]