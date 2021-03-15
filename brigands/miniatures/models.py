from django.db import models

from factions.models import Faction


class Chassis(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    manufacturer = models.CharField(max_length=100, blank=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Variant(models.Model):
    chassis = models.ForeignKey(Chassis, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    threat_value = models.IntegerField(null=True)
    unit_availability = models.CharField(max_length=100, blank=True)
    armour = models.IntegerField()
    hull = models.IntegerField()
    structure = models.IntegerField()
    actions = models.IntegerField()
    gunnery = models.IntegerField()
    piloting = models.IntegerField()
    type = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)
    primary_movement = models.CharField(max_length=100, blank=True)
    secondary_movement = models.CharField(max_length=100, blank=True)
    sensors = models.IntegerField()

    primary_role = models.CharField(max_length=100, blank=True)
    secondary_role = models.CharField(max_length=100, blank=True)

    is_stock = models.BooleanField()
    is_also_leagueless = models.BooleanField()
    is_in_brigands_release = models.BooleanField()

    added_notes = models.CharField(max_length=100, blank=True)
    build_notes = models.CharField(max_length=100, blank=True)
    generic_notes = models.CharField(max_length=100, blank=True)
    tv_notes = models.CharField(max_length=100, blank=True)

    alternative_names = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    debut_notes = models.CharField(max_length=100, blank=True)
    debut_year = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
