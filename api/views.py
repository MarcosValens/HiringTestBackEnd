from django.db.models import Count, Q

import json
import numpy as np
import pandas as pd
import geojson

from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from geojson import Point, Feature, FeatureCollection, dump

from rest_framework import viewsets
from .models import HotelInfo
from .models import HotelReviews
from .serializer import HotelInfoSerializer
from .serializer import HotelReviewSerializer


class HotelInfoViewSet(viewsets.ModelViewSet):
    geolocator = Nominatim(user_agent='http')
    geocode_with_delay = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    queryset = HotelInfo.objects.filter(review_qty__lte=5)
    query = queryset.values('hotel_address')
    df = pd.DataFrame.from_records(query)
    df = df.loc[520:523]  # I do this line because it takes too long the geocode all results
    df['temp'] = df['hotel_address'].apply(geocode_with_delay)
    df['coords'] = df['temp'].apply(lambda loc: tuple(loc.point) if loc else None)
    dfCoords = df['coords']
    dfCoords = dfCoords.tolist()
    dumpdf = pd.DataFrame(dfCoords, columns=['long', 'lat', 'elev']).dropna()


    def data2geojson(df):
        try:
            features = []
            df.apply(lambda X: features.append(
                geojson.Feature(geometry=geojson.Point((X["lat"],
                                                    X["long"],
                                                    X["elev"])),
                            properties={"country": "Spain"})), axis=1)
            with open('map.geojson', 'w') as fp:
                geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True)
        except ValueError:
            print('Out of range float values are not JSON compliant: nan')

    data2geojson(dumpdf)
    serializer_class = HotelInfoSerializer


class HotelReviewsViewSet(viewsets.ModelViewSet):
    queryset = HotelReviews.objects.filter(review_date__range=('2018-01-01', '2019-12-12')).filter(
        hotel__review_qty__lte=5).select_related('hotel')
    # queryset = HotelReviews.objects.filter( review_date__range=('2019-01-01', '2019-12-31')).values(
    # 'hotel').annotate(review_qty=Count('hotel_id')).filter( review_qty__gte=5)

    serializer_class = HotelReviewSerializer
