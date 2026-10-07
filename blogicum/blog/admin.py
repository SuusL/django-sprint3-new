
from django.contrib import admin

from .models import Post, Category, Location

admin.site.register([Post, Category, Location])
