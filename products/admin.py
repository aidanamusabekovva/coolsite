# Register your models here.
from django.contrib import admin
from products.models import Products, Animal

admin.site.register(Products)

admin.site.register(Animal)