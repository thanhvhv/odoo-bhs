from django.db import models
from datetime import timedelta

# Create your models here.
class Odoo(models.Model):
    name = models.CharField(max_length=50)
    version = models.IntegerField()
    
    def __str__(self):
        return self.name
    


class Demo(models.Model):
    name = models.CharField(max_length=100)
    version = models.ForeignKey(Odoo, on_delete=models.CASCADE)
    port = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(default=timedelta(hours=1))
    STATE_CHOICES = {
    "Starting": "Starting",
    "Running": "Running",
    "Stopped": "Stopped",
    "Destroyed": "Destroyed",
    }
    state = models.CharField(max_length=15, choices=STATE_CHOICES, default="Starting")


    def __str__(self):
        return self.name
    
class Module(models.Model):
    odoo = models.ForeignKey(Odoo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    demo = models.ManyToManyField(Demo)

    def __str__(self):
        return self.name
    
class Port(models.Model):
    port = models.IntegerField()
    url = models.CharField(max_length=150, blank=True)
