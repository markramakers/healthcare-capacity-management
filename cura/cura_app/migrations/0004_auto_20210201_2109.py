# Generated by Django 3.1.5 on 2021-02-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cura_app', '0003_auto_20210201_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocationrequest',
            name='allocation_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Eind datum'),
        ),
        migrations.AlterField(
            model_name='bedclientallocations',
            name='allocation_end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Eind datum'),
        ),
    ]
