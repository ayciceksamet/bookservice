from django.db import models

class Room(models.Model):
    roomid = models.CharField(max_length=60)
    max_numberofpeople = models.IntegerField(max_length=60,null=True)


class IntervalData(models.Model):
    fromTime = models.DateTimeField()
    toTime = models.DateTimeField()
    roomidstored = models.ForeignKey(Room, related_name='roompickup', on_delete=models.CASCADE,null=True)

