# Generated by Django 2.2.7 on 2021-01-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniatures', '0002_auto_20210124_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='added_notes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='alternative_names',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='build_notes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='debut_notes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='debut_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='generic_notes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='height',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='primary_movement',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='primary_role',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='secondary_movement',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='secondary_role',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='tv_notes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='variant',
            name='unit_availability',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
