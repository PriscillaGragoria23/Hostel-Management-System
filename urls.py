from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from schoolapp import views
from django.urls import include, path


urlpatterns = [
path('',views.logindetails,name='logindetails'),
path('admin/',views.admindashboard,name='admindashboard'),
path('register/',views.register,name='register'),
path('dashboard/',views.dashboard,name='dashboard'),
path('gallery/',views.gallery,name='gallery'),
path('booking/',views.Booking,name='booking'),
path('tarrif/',views.tariffdetails,name='tariffdetails'),
path('onlinebk/',views.onlinebooking,name='onlinebooking'),
path('offlinebk/',views.offlinebooking,name='offlinebooking'),
path('management/',views.management,name='management'),
path('rooms/',views.rooms,name='rooms'),
path('updation/',views.updation,name='updation'),
path('bookeddetails/',views.bookeddetails,name='bookeddetails'),
path('offregister/',views.offregister,name='offregister'),
path('roomallotment/',views.roomallotment,name='roomallotment'),
path('offline_reg_det/',views.off_reg_det,name='off_reg_det'),
path('managementdetails/',views.managementdetails,name='managementdetails'),
path('myadmin/',admin.site.urls)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


