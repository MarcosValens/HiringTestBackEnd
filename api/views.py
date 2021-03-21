from django.db.models import Count, Q

import os
import json
import pandas as pd
import geojson

from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HotelInfo
from .models import HotelReviews
from .serializer import HotelInfoSerializer
from .serializer import HotelReviewSerializer


class HelloAPIView(APIView):
    def get(self, request, format=None):
        with open('./map.geojson') as f:
            data = json.load(f)
        return Response(data)


class HotelInfoViewSet(viewsets.ModelViewSet):

    def dataframe_creator(query):
        geolocator = Nominatim(user_agent='http')
        geocode_with_delay = RateLimiter(geolocator.geocode, min_delay_seconds=1)
        df = pd.DataFrame.from_records(query)
        # df = df.loc[520:525]  # I do this line because it takes too long the geocode all results
        df['temp'] = df['hotel_address'].apply(geocode_with_delay)
        df['coords'] = df['temp'].apply(lambda loc: tuple(loc.point) if loc else None)
        new_df = df[['coords', 'country_area']].dropna()
        coords_list = new_df['coords'].tolist()
        df = pd.DataFrame(coords_list, columns=['long', 'lat', 'elev']).dropna()
        new_df.index = df.index
        df['country_area'] = new_df['country_area']
        return df

    def data2geojson(df):
        try:
            features = []
            df.apply(lambda data: features.append(
                geojson.Feature(geometry=geojson.Point((data["lat"],
                                                        data["long"],
                                                        data["elev"])),
                                properties={"country_area": data["country_area"]})), axis=1)
            with open('map.geojson', 'w') as fp:
                geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True)
        except ValueError:
            print('Out of range float values are not JSON compliant: nan')

    queryset = HotelInfo.objects.filter(review_qty__lte=5)
    query = queryset.values('hotel_address', 'country_area')
    if os.path.exists('../map.geojson') or os.path.getsize('../map.geojson') == 0:
        df = dataframe_creator(query)
        data2geojson(df)
    serializer_class = HotelInfoSerializer


class HotelReviewsViewSet(viewsets.ModelViewSet):
    queryset = HotelReviews.objects.filter(review_date__range=('2018-01-01', '2019-12-12')).filter(
        hotel__review_qty__lte=5).select_related('hotel')
    # queryset = HotelReviews.objects.filter( review_date__range=('2019-01-01', '2019-12-31')).values(
    # 'hotel').annotate(review_qty=Count('hotel_id')).filter( review_qty__gte=5)

    serializer_class = HotelReviewSerializer
