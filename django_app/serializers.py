from rest_framework import serializers
from .models import User, Home, Favorite
from django.contrib.auth.hashers import make_password

class HomeObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('id', 'photo', 'price', 'bed', 'bath', 'street', 'city', 'state', 'zip_code', 'lat', 'log')

class UserObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'social_level', 'hobbies', 'budget', 'current_rent', 'lease_end')

class FavoriteObjectSerializer(serializers.ModelSerializer):
    home = HomeObjectSerializer(many=False)

    class Meta:
        model = Favorite
        fields = ('home', 'id')

class UserSerializer(serializers.ModelSerializer):
    favorites = FavoriteObjectSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'phone_number', 'social_level', 'hobbies','budget', 'current_rent', 'lease_end', 'favorites')
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            password = make_password(validated_data['password']),
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            social_level = validated_data['social_level'],
            hobbies = validated_data['hobbies'],
            budget = validated_data['budget'],
            current_rent = validated_data['current_rent'],
            lease_end = validated_data['lease_end'],
        )

        user.save()

        return user

class HomeSerializer(serializers.ModelSerializer):
    users = UserObjectSerializer(many=True)
    
    class Meta:
        model = Home
        fields = ('id', 'photo', 'price', 'bed', 'bath', 'street', 'city', 'state', 'zip_code', 'lat', 'log', 'users')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'home', 'user')