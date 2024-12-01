from django.contrib import admin
from .models import registration,login,booking_online,profile_updation, roomdetails_online,room_allotment,offline_registration,inventory,accounts

# Register your models here.
admin.site.register(registration)
admin.site.register(login)
admin.site.register(booking_online)
admin.site.register(profile_updation)
admin.site.register(room_allotment)
admin.site.register(roomdetails_online)
admin.site.register(offline_registration)
admin.site.register(inventory)
admin.site.register(accounts)
