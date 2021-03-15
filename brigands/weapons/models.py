from django.db import models

class WeaponType(models.Model):
    name = models.CharField(max_length=100)
    range = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    melee_capable = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Weapon(models.Model):
    code = models.CharField(max_length=100)
    penetration = models.IntegerField()
    traits = models.CharField(max_length=100)
    type = models.ForeignKey(WeaponType, on_delete=models.CASCADE)
    weight = models.CharField(max_length=100)

    def __str__(self):
        return self.code
