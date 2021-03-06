from rest_framework import serializers
from .models import User, Home, Favorite
from django.contrib.auth.hashers import make_password

class HomeObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'property_id', 'listing_id', 'rdc_web_url', 'prop_type', 'href', 'city', 'line', 'postal_code', 'state_code', 'state', 'fips_code', 'lat', 'lon', 'neighborhood_name', 'prop_status', 'price', 'baths_full', 'baths', 'beds', 'size', 'units', 'photo_count', 'thumbnail', 'page_no', 'rank', 'mls_id', 'abbreviation')

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'name', 'phone_number', 'social_level', 'hobbies', 'budget', 'current_rent', 'income', 'occupation', 'lease_end', 'marital_status', 'picture')

class FavoriteObjectSerializer(serializers.ModelSerializer):
    home = HomeObjectSerializer(many=False)

    class Meta:
        model = Favorite
        fields = ('home', 'id')

class UserSerializer(serializers.ModelSerializer):
    favorites = FavoriteObjectSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'name', 'phone_number', 'social_level', 'hobbies', 'budget', 'current_rent', 'income', 'occupation', 'lease_end', 'marital_status', 'picture', 'favorites')
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            email = validated_data['email'],
            name = validated_data['name'],
            phone_number = validated_data['phone_number'],
            social_level = validated_data['social_level'],
            hobbies = validated_data['hobbies'],
            budget = validated_data['budget'],
            current_rent = validated_data['current_rent'],
            income = validated_data['income'],
            occupation = validated_data['occupation'],
            lease_end = validated_data['lease_end'],
            marital_status = validated_data['marital_status'],
            picture = validated_data['picture']
        )

        user.save()

        return user

class HomeSerializer(serializers.ModelSerializer):
    users = UserObjectSerializer(many=True)
    favorites = FavoriteObjectSerializer(many=True)
    
    class Meta:
        model = Home
        fields = ('id', 'property_id', 'listing_id', 'rdc_web_url', 'prop_type', 'href', 'city', 'line', 'postal_code', 'state_code', 'state', 'fips_code', 'lat', 'lon', 'neighborhood_name', 'prop_status', 'price', 'baths_full', 'baths', 'beds', 'size', 'units', 'photo_count', 'thumbnail', 'page_no', 'rank', 'mls_id', 'abbreviation', 'users', 'favorites')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'home', 'user')