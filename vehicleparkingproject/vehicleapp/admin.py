from django.contrib import admin
from .models import Profiles,Vehicles,CREDIT_CARDS,PARKING_LOTS,PARKING_RESERVATIONS,PARKING_SPACES
# Register your models here.
admin.site.register(Profiles)
admin.site.register(Vehicles)
admin.site.register(CREDIT_CARDS)
admin.site.register(PARKING_LOTS)
admin.site.register(PARKING_RESERVATIONS)
admin.site.register(PARKING_SPACES)
