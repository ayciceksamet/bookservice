# Generated by Django 3.0.4 on 2020-07-05 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RoomApp', '0003_auto_20200705_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromTime', models.DateTimeField()),
                ('toTime', models.DateTimeField()),
                ('roomstored', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roompickup', to='RoomApp.Room')),
            ],
        ),
    ]
