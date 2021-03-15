import csv
from django.core.management import BaseCommand
from weapons.models import Weapon, WeaponType

class Command(BaseCommand):
    help = 'Load a weapons csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            next(reader, None)
            for row in reader:
                categories = row[0]
                code = row[1]
                melee = row[2]
                pen = row[3]
                range = row[4]
                traits = row[5]
                type = row[6]
                weapon_id = row[7]
                weight = row[8]

                type_code = code[2:] if code[0] == "V" else code[1:]
                melee_capable = True if melee == "Yes" else False
                penetration = int(pen)

                weapon_type, created = WeaponType.objects.get_or_create(
                    name=type,
                    range=range,
                    categories=categories,
                    code=type_code,
                    melee_capable=melee_capable
                )

                Weapon.objects.create(
                    code=code,
                    penetration=penetration,
                    traits=traits,
                    type=weapon_type,
                    weight=weight
                )

    def get_weight(code):
        if code[0] == "L":
            return "Light"
        if code[0] == "M":
            return "Medium"
        if code[0] == "H":
            return "Heavy"
        if code[0:1] == "VL":
            return "Very Light"
        if code[0:1] == "VH":
            return "Very Heavy"
        return "UNRECOGNISED WEIGHT"