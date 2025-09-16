from django.contrib import admin

from .models import Car, Comment, Country, Manufacturer


admin.site.register(Car)
admin.site.register(Comment)
admin.site.register(Country)
admin.site.register(Manufacturer)
