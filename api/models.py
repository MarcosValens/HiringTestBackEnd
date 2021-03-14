from django.db import models


class HotelInfo(models.Model):
    country_area = models.CharField(max_length=45)
    hotel_id = models.CharField(primary_key=True, max_length=32)
    hotel_name = models.TextField(blank=True, null=True)
    hotel_url = models.TextField(blank=True, null=True)
    hotel_address = models.TextField(blank=True, null=True)
    review_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    review_qty = models.IntegerField(blank=True, null=True)
    clean = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    comf = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    loct = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fclt = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    staff = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    vfm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    wifi = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_info'
        unique_together = (('hotel_id', 'country_area'),)
        verbose_name_plural = "hotels"


class HotelReviews(models.Model):
    uuid = models.CharField(primary_key=True, db_column='UUID', max_length=36, blank=True)
    hotel = models.ForeignKey(HotelInfo, on_delete=models.CASCADE)
    review_title = models.TextField(blank=True, null=True)
    review_url = models.TextField(blank=True, null=True)
    review_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    reviewer_name = models.TextField(blank=True, null=True)
    hash_reviewer_name = models.CharField(max_length=200, blank=True, null=True)
    reviewer_location = models.CharField(max_length=100, blank=True, null=True)
    posting_conts = models.IntegerField(blank=True, null=True)
    positive_content = models.TextField(blank=True, null=True)
    negative_content = models.TextField(blank=True, null=True)
    tag_n1 = models.TextField(blank=True, null=True)
    tag_n2 = models.TextField(blank=True, null=True)
    tag_n3 = models.TextField(blank=True, null=True)
    tag_n4 = models.TextField(blank=True, null=True)
    tag_n5 = models.TextField(blank=True, null=True)
    staydate = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hotel_reviews'
        verbose_name_plural = "Reviews"
