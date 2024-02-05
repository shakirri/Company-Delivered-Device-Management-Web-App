from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20, primary_key=True, serialize=False)

class Brand(models.Model):
    brand=models.CharField(max_length=20, primary_key=True, serialize=False)
    
class Devices(models.Model):
    deviceID=models.CharField(max_length=20, primary_key=True, serialize=False)
    deviceName=models.CharField(default=None, blank=True, null=True, max_length=20)
    type=models.CharField(default=None, blank=True, null=True, max_length=11)
    brand=models.ForeignKey(Brand)
    condition=models.CharField(default=None, blank=True, null=True, max_length=11)
    
    
class Employees(models. Model):
        empID=models.CharField(max_length=20, primary_key=True, serialize=False)
        name=models.ForeignKey(Company)
        deviceID=models.ForeignKey(Devices)