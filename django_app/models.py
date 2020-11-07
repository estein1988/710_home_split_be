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
    photo = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    bed = models.IntegerField()
    bath = models.IntegerField()
    street = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=15)
    lat_long = models.JSONField(default=dict)
    lat = models.FloatField(null=True)
    log = models.FloatField(null=True)
    users = models.ManyToManyField(User, related_name='users', through='Favorite')

    def __str__(self):
        return f'{self.id}: {self.street}'


class Favorite(models.Model):
    home = models.ForeignKey(Home, blank=True, null=True, related_name='favorites', on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, null=True, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}'