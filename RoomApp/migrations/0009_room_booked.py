# Generated by Django 3.0.4 on 2020-07-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomApp', '0008_room_capacityofroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='booked',
            field=models.BooleanField(default=False),
        ),
    ]
