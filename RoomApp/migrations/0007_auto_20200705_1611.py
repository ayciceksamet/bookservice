# Generated by Django 3.0.4 on 2020-07-05 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RoomApp', '0006_intervaldata_roomidstored'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='max_numberofpeople',
            field=models.IntegerField(max_length=60, null=True),
        ),
    ]