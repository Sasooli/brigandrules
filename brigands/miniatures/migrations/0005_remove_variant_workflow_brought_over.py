# Generated by Django 2.2.7 on 2021-01-24 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniatures', '0004_variant_chassis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='workflow_brought_over',
        ),
    ]
