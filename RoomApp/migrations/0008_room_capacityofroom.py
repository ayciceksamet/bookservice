# Generated by Django 3.0.4 on 2020-07-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomApp', '0007_auto_20200705_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='capacityOfRoom',
            field=models.IntegerField(max_length=60, null=True),
        ),
    ]
