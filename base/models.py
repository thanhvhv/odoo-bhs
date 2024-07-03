from django.db import models

# Create your models here.
class Odoo(models.Model):
    name = models.CharField(max_length=50)
    version = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Module(models.Model):
    odoo = models.ForeignKey(Odoo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Demo(models.Model):
    odoo = models.ForeignKey(Odoo, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name