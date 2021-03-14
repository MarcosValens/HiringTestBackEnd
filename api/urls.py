from django.urls import path, include
from rest_framework import routers

from .views import HotelInfoViewSet
from .views import HotelReviewsViewSet

router = routers.DefaultRouter()
router.register(r'hotels', HotelInfoViewSet)
router.register(r'reviews', HotelReviewsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
