from django.contrib import admin

from .models import Chassis, Variant

admin.site.register(Chassis)
admin.site.register(Variant)