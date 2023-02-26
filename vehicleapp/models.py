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
    
    
class Credit_Cards(models.Model):
    users_id=models.ForeignKey(Profiles,on_delete=models.CASCADE)
    card_number=models.IntegerField(10)
    cardholder_name=models.CharField(max_length=200)
    expiration_date=models.DateField()
    is_default=models.BooleanField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    

class Parking_Lots(models.Model):
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    total_spaces=models.IntegerField()
    available_space=models.IntegerField()
    is_active=models.BooleanField()
    created_at=models.BooleanField()
    updated_at=models.BooleanField()
    
    
class Parking_Reservations(models.Model):
    users_id=models.ForeignKey(Profiles,on_delete=models.CASCADE)
    parking_space_id=models.ForeignKey(Parking_Lots,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    is_active=models.BooleanField()
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()
    exited_at=models.DateTimeField()
    
    
    def __str__(self):
        return self.start_time

