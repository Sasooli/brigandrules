from django.contrib import admin

from .models import Weapon, WeaponType

admin.site.register(Weapon)
admin.site.register(WeaponType)