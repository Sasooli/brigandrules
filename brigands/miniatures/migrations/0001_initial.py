# Generated by Django 2.2.7 on 2021-01-24 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('factions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('threat_value', models.IntegerField()),
                ('unit_availability', models.CharField(max_length=100)),
                ('armour', models.IntegerField()),
                ('hull', models.IntegerField()),
                ('structure', models.IntegerField()),
                ('actions', models.IntegerField()),
                ('gunnery', models.IntegerField()),
                ('piloting', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('primary_movement', models.CharField(max_length=100)),
                ('secondary_movement', models.CharField(max_length=100)),
                ('sensors', models.IntegerField()),
                ('primary_role', models.CharField(max_length=100)),
                ('secondary_role', models.CharField(max_length=100)),
                ('is_stock', models.BooleanField()),
                ('is_also_leagueless', models.BooleanField()),
                ('is_in_brigands_release', models.BooleanField()),
                ('workflow_brought_over', models.BooleanField()),
                ('added_notes', models.CharField(max_length=100)),
                ('build_notes', models.CharField(max_length=100)),
                ('generic_notes', models.CharField(max_length=100)),
                ('tv_notes', models.CharField(max_length=100)),
                ('alternative_names', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('debut_notes', models.CharField(max_length=100)),
                ('debut_year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Chassis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('manufacturer', models.CharField(max_length=100)),
                ('faction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factions.Faction')),
            ],
        ),
    ]
