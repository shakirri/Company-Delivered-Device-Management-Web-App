from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=20, primary_key=True, serialize=False)

class Brand(models.Model):
    brand=models.CharField(max_length=20, primary_key=True, serialize=False)

class Employees(models. Model):
    empID=models.CharField(max_length=20, primary_key=True, serialize=False)
    empName=models.CharField(default=None, blank=True, null=True, max_length=20)
    name=models.ForeignKey(Company, on_delete=models.CASCADE)
    
class Devices(models.Model):
    deviceID=models.CharField(max_length=20, primary_key=True, serialize=False)
    deviceName=models.CharField(default=None, blank=True, null=True, max_length=20)

    class DTypes(models.TextChoices):
        Phones='Phones'
        Tablets='Tablets'
        Laptops='Laptops'
        Others='Others'

    dType=models.CharField(default=None, choices=DTypes.choices, max_length=10)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    empID=models.ForeignKey(Employees, on_delete=models.CASCADE)

    class Conditions(models.TextChoices):
        New='New'
        Mint='Mint'
        Good='Good'
        Broken='Broken'
        Damaged='Damaged'

    handedCondition=models.CharField(default='New', choices=Conditions.choices, max_length=10)
    returnedCondition=models.CharField(default='Good', blank=True, null=True, max_length=11)
    checkOut=models.DateField()
    returned=models.DateField()