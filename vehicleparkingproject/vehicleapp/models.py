from django.db import models

# Create your models here.
class Profiles(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    phone_number=models.IntegerField()

    def __str__(self):
        return self.first_name

class Vehicles(models.Model):
    vehicle_name=models.CharField(max_length=200)
    plate_number=models.CharField(max_length=10)
    color=models.CharField(max_length=10)
    is_active=models.BooleanField()
    entry_date= models.DateTimeField()
    updated_date=models.DateTimeField()
    exit_date=models.DateTimeField()

    def __str__(self):
        return self.vehicle_name
