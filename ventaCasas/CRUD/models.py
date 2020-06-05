from django.db import models

# Create your models here.

class houses(models.Model):
    id = models.AutoField(primary_key = True)
    location = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    area = models.IntegerField()
    rooms = models.IntegerField()
    bathRooms = models.IntegerField()
    parking = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(default='none.png')

