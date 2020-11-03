from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('homes', views.HomeView)
router.register('favorites', views.FavoriteView)
router.register('profile', views.ProfileView)

urlpatterns = [
    path('', include(router.urls))
]