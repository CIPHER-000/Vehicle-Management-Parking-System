from django.contrib import admin
from .models import Profiles,Vehicles,Credit_Cards,Parking_Lots,Parking_Reservations
# Register your models here.
admin.site.register(Profiles)
admin.site.register(Vehicles)
admin.site.register(Credit_Cards)
admin.site.register(Parking_Lots)
admin.site.register(Parking_Reservations)



