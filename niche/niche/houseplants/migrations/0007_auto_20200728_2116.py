# Generated by Django 3.0.4 on 2020-07-28 21:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houseplants', '0006_activity_plantlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='image',
            field=models.ImageField(default='default.gif', upload_to=''),
        ),
        migrations.AlterField(
            model_name='plantlog',
            name='date',
            field=models.DateField(default=datetime.date(2020, 7, 28)),
        ),
        migrations.AlterField(
            model_name='plantlog',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houseplants.Plant'),
        ),
    ]
