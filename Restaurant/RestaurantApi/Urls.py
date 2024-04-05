from django.urls import path
from .views import CreateRestaurant, RestaurantDetails, CreateOwner, OwnerDetails
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('restaurants/', CreateRestaurant.as_view(), name='create-restaurant'),
    path('restaurants/<int:id>/', RestaurantDetails.as_view(), name='restaurant-detail'),
    path('owners/', CreateOwner.as_view(), name='register-owner'),
    path('owners/<int:id>/', OwnerDetails.as_view(), name='owner-detail'),
]