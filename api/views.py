from django.db.models import Count, Q

from rest_framework import viewsets
from .models import HotelInfo
from .models import HotelReviews
from .serializer import HotelInfoSerializer
from .serializer import HotelReviewSerializer


class HotelInfoViewSet(viewsets.ModelViewSet):
    queryset = HotelInfo.objects.filter(review_qty__lte=5)
    serializer_class = HotelInfoSerializer


class HotelReviewsViewSet(viewsets.ModelViewSet):
    queryset = HotelReviews.objects.filter(review_date__range=('2018-01-01', '2019-12-12')).filter(
        hotel__review_qty__lte=5).select_related('hotel')
    # queryset = HotelReviews.objects.filter(
    #     review_date__range=('2019-01-01', '2019-12-31')).values('hotel').annotate(review_qty=Count('hotel_id')).filter(
    #     review_qty__gte=5)
    print(queryset.query)
    serializer_class = HotelReviewSerializer



