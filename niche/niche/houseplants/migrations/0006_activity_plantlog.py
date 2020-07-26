# Generated by Django 3.0.4 on 2020-07-26 10:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houseplants', '0005_remove_plant_full_sun'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default=' ', max_length=50)),
                ('description', models.TextField(default='Activity Description', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PlantLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date(2020, 7, 26))),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houseplants.Activity')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houseplants.Plant')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
