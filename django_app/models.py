from django.db import models
from django.contrib.auth.models import User, AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    social_level = models.CharField(max_length=50, null=True)
    hobbies = models.CharField(max_length=250, null=True)
    budget = models.CharField(max_length=50, null=True)
    current_rent = models.CharField(max_length=50, null=True)
    income = models.CharField(max_length=50, null=True)
    occupation = models.CharField(max_length=50, null=True)
    lease_end = models.CharField(max_length=50, null=True)
    marital_status = models.CharField(max_length=50, null=True)
    picture = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.username

class Home(models.Model):
    property_id = models.CharField(max_length=50, null=True)
    listing_id = models.CharField(max_length=50, null=True)
    rdc_web_url = models.CharField(max_length=250, null=True)
    prop_type = models.CharField(max_length=100, null=True)
    href = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=25, null=True)
    line = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=15, null=True)
    state_code = models.CharField(max_length=15, null=True)
    state = models.CharField(max_length=15, null=True)
    fips_code = models.CharField(max_length=15, null=True)
    lat = models.FloatField(null=True)
    lon = models.FloatField(null=True)
    neighborhood_name = models.CharField(max_length=100, null=True)
    prop_status = models.CharField(max_length=100, null=True)
    price = models.IntegerField(null=True)
    baths_full = models.IntegerField(null=True)
    baths = models.IntegerField(null=True)
    beds = models.IntegerField(null=True)
    size = models.IntegerField(null=True)
    units = models.CharField(max_length=15, null=True)
    photo_count = models.IntegerField(null=True)
    thumbnail = models.CharField(max_length=250, null=True)
    page_no = models.IntegerField(null=True)
    rank = models.CharField(max_length=15, null=True)
    mls_id = models.CharField(max_length=15, null=True)
    abbreviation = models.CharField(max_length=15, null=True)
    users = models.ManyToManyField(User, related_name='users', through='Favorite')

    def __str__(self):
        return f'{self.id}: {self.line}'


class Favorite(models.Model):
    home = models.ForeignKey(Home, blank=True, null=True, related_name='favorites', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'