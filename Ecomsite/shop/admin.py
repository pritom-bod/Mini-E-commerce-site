from django.contrib import admin
from .models import Products, order

# Register your models here.

admin.site.register(Products)

admin.site.register(order)