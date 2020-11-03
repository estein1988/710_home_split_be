from django.contrib import admin
from .models import User, Home, Favorite

# Register your models here.
admin.site.register(User)
admin.site.register(Home)
admin.site.register(Favorite)