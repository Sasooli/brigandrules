import csv
from django.core.management import BaseCommand
from miniatures.models import Chassis
from factions.models import Faction

class Command(BaseCommand):
    help = 'Load a chassis csv file into the database; also creates factions'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            next(reader, None)
            for row in reader:
                id = row[0]
                name = row[1]
                faction_name = row[2]
                description = row[3]
                manufacturer = row[4]

                faction, created = Faction.objects.get_or_create(
                    name=faction_name
                )

                Chassis.objects.create(
                    pk=id,
                    name=name,
                    description=description,
                    manufacturer=manufacturer,
                    faction=faction
                )
