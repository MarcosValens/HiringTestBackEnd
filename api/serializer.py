from rest_framework import serializers

from .models import HotelInfo
from .models import HotelReviews


class HotelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelInfo
        fields = '__all__'


class HotelReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelReviews
        fields = '__all__'
