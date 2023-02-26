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

class CREDIT_CARDS(models.Model):
    card_number= models.IntegerField()
    cardholder_name= models.CharField(max_length=200)
    expiration_date= models.DateTimeField()
    is_default= models.BooleanField()
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()

    def __str__(self):
        return self.card_number
    
class PARKING_LOTS(models.Model):
    parking_name = models.CharField(max_length=200)
    locations = models.CharField(max_length=200)
    total_spaces= models.IntegerField()
    available_spaces= models.IntegerField()
    is_active = models.BooleanField()
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()

    def __str__(self):
        return self.parking_name
    
class PARKING_SPACES(models.Model):
    parking_space_name= models.CharField(max_length=200)
    is_available= models.BooleanField()
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()

    def __str__(self):
        return self.parking_space_name
    
class PARKING_RESERVATIONS(models.Model):
    start_time= models.DateTimeField()
    end_time= models.DateTimeField()
    is_active= models.BooleanField()
    created_date=models.DateTimeField()
    updated_date=models.DateTimeField()

    def __str__(self):
        return self.start_time

