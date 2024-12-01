from django.db import models
from django.utils import timezone
class registration(models.Model):
    regname = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    num = models.BigIntegerField()
    uname = models.CharField(max_length=200)
    psw = models.CharField(max_length=30)
    role = models.CharField(max_length=30,default='none')
    psw_repeat = models.CharField(max_length=30)


class login(models.Model):
    uname = models.CharField(max_length=200)
    psw = models.CharField(max_length=300)
    role = models.CharField(max_length=30,default='NONE')
    login_time = models.DateTimeField(default=timezone.now)


class booking_online(models.Model):
    regno=models.IntegerField(default=0)
    nameon= models.CharField(max_length=100,default='none')
    age= models.IntegerField(default=0)
    fname= models.CharField(max_length=200,default='none')
    occ= models.CharField(max_length=30,default='none')
    mob= models.CharField(max_length=30,default='none')
    email= models.CharField(max_length=200,default='none')
    stay_period=models.CharField(max_length=200,default='none')
    doj = models.CharField(max_length=100,default='none')
    rooms=models.CharField(max_length=100,default='none')
    food=models.CharField(max_length=100,default='none')
    ac=models.CharField(max_length=200,default='none')
    amt = models.IntegerField(default=0)
    pay_mode=models.CharField(max_length=200,default='none')
    PROOF=models.CharField(max_length=200,default='none')
    idnum=models.BigIntegerField(default=0)

class roomdetails_online(models.Model):
    room_type=models.CharField(max_length=200)
    ac_nonac= models.CharField(max_length=100)
    total_rooms= models.IntegerField()
    booked_rooms= models.IntegerField()
    available_rooms= models.IntegerField()
    price_per_month= models.IntegerField()
    food_cost= models.IntegerField()
    total_price = models.IntegerField()

class profile_updation(models.Model):
    img1=models.ImageField(upload_to='photos/')
    img2= models.ImageField(upload_to='photos/')
    img3= models.ImageField(upload_to='photos/')
    img4= models.ImageField(upload_to='photos/')
    video= models.FileField(upload_to='videos/')


class offline_registration(models.Model):
    offreg=models.IntegerField()
    offname= models.CharField(max_length=100)
    offage= models.IntegerField()
    father= models.CharField(max_length=100)
    occupation= models.CharField(max_length=100)
    mobile= models.BigIntegerField()
    off_email= models.CharField(max_length=200)
    p_o_stayy = models.CharField(max_length=200)
    stay_period = models.CharField(max_length=200)
    date_of_join = models.DateField(max_length=100)
    rooms = models.CharField(max_length=20)
    food = models.CharField(max_length=200)
    ac = models.CharField(max_length=30)
    PROOF = models.CharField(max_length=30)
    idnum = models.IntegerField()
    amt = models.IntegerField()
    mode = models.CharField(max_length=100)
class room_allotment(models.Model):
    roomno=models.IntegerField()
    client= models.CharField(max_length=100)
    roomtype= models.CharField(max_length=200)
    roomnature= models.CharField(max_length=100)

class inventory(models.Model):
    things=models.CharField(max_length=20)
    number_of_items= models.IntegerField()
    room_num= models.IntegerField()
class accounts(models.Model):
    collection = models.IntegerField()
    expenses = models.IntegerField()
    income = models.IntegerField()





