from django.db import models

# Create your models here.

class Activitie(models.Model):
    name = models.CharField(max_length=9999)
    price = models.CharField(max_length=9999)
    date = models.CharField(max_length=9999)
    startHour = models.CharField(max_length=9999)
    typ = models.CharField(max_length=9999)
    timeToLong = models.CharField(max_length=9999)
    Long = models.CharField(max_length=9999)
    Url = models.CharField(max_length=9999)
    point = models.IntegerField(default = 0)
         

class UsersPage(models.Model):
    user = models.CharField(max_length=9999,primary_key=True)
    activities = models.ManyToManyField(Activitie)
    name = models.CharField(max_length=9999)
    background = models.CharField(max_length=9999,default = '#396b83')
    text = models.CharField(max_length=9999,default='#555555')

class Publication(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(UsersPage)
    activities = models.ForeignKey(Activitie)
