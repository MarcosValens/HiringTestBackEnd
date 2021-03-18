from django.urls import path, include
from rest_framework import routers

from .views import HotelInfoViewSet
from .views import HotelReviewsViewSet
from .views import HelloAPIView

router = routers.DefaultRouter()
router.register(r'hotels', HotelInfoViewSet)
router.register(r'reviews', HotelReviewsViewSet)


urlpatterns = [
    path('hello/', HelloAPIView.as_view()),
    path('', include(router.urls))
]
