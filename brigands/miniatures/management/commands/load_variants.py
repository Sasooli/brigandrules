import csv
from django.core.management import BaseCommand
from miniatures.models import Chassis, Variant

class Command(BaseCommand):
    help = 'Load a variants (models) csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            next(reader, None)
            for row in reader:
                model_id = row[0]
                chassis_name = row[1]
                name = row[2]
                threat_value = row[3]
                unit_availability = row[4]
                armour = row[5]
                hull = row[6]
                structure = row[7]
                actions = row[8]
                gunnery = row[9]
                piloting = row[10]
                type = row[11]
                height = row[12]
                primary_movement = row[13]
                secondary_movement = row[14]
                added_notes = row[15]
                generic_notes = row[16]
                workflow_flag = row[17]
                build_notes = row[18]
                primary_role = row[19]
                secondary_role = row[20]
                tv_notes = row[21]
                is_also_leagueless = row[22]
                is_in_brigands_release = row[23]
                sensors = row[24]
                description = row[25]
                alternative_names = row[26]
                is_stock = row[27]
                debut_year = row[28]
                debut_notes = row[29]


                try:
                    chassis = Chassis.objects.get(name=chassis_name)

                    Variant.objects.create(
                        name = name,
                        threat_value = None if threat_value == '' else int(threat_value),
                        unit_availability = unit_availability,
                        armour = int(armour),
                        hull = int(hull),
                        structure = int(structure),
                        actions = int(actions),
                        gunnery = int(gunnery),
                        piloting = int(piloting),
                        type = type,
                        height = height,
                        primary_movement = primary_movement,
                        secondary_movement = secondary_movement,
                        sensors = int(sensors[:-1]),

                        primary_role = primary_role,
                        secondary_role = secondary_role,

                        is_stock = is_stock == "Yes",
                        is_also_leagueless = is_also_leagueless == "Yes",
                        is_in_brigands_release = is_in_brigands_release == "Yes",

                        added_notes = added_notes,
                        build_notes = build_notes,
                        generic_notes = generic_notes,
                        tv_notes = tv_notes,
                        alternative_names = alternative_names,
                        description = description,
                        debut_notes = debut_notes,
                        debut_year = debut_year,

                        chassis=chassis
                    )

                except Exception as e:
                  print("Error with variant " + name)
                  print(e)
