from django.shortcuts import render,redirect
from .models import registration,login,booking_online,profile_updation, roomdetails_online,room_allotment,offline_registration,inventory,accounts
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages


# Create your views here.
def logindetails(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        psw = request.POST.get('psw')
        role = request.POST.get('role')
        try:
            faculty = registration.objects.get(uname=uname)
            if psw == faculty.psw:  # Compare with faculty.psw, not registration.psw
                hashed_psw = faculty.psw  # Use faculty.psw, not registration.psw

                login.objects.create(
                        uname=uname,
                        psw=hashed_psw,
                        role=role,
                )
                if role == 'user':
                    return redirect('dashboard')
                else:
                    return redirect('admindashboard')
            # If faculty is not registered, render the login page with a message
            elif psw != faculty.psw:  # Compare with faculty.psw, not registration.psw
               messages.error(request,'invalid password')
        except registration.DoesNotExist:
            messages.error(request,"you have not registered yet")
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        regname =request.POST['regname']
        email =request.POST['email']
        num =request.POST['num']
        uname = request.POST['uname']
        psw = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        role = request.POST['role']
        if psw != psw_repeat:
            messages.error(request,'error in your password')
        else:

            registration.objects.create(
            regname=regname,
            email=email,
            num=num,
            uname=uname,
            psw=psw,
            psw_repeat=psw_repeat,
            role=role
            )
            return redirect('logindetails')

    return render(request,'Registration.html')
def dashboard(request):
    return render(request,'Dashboard.html')
def admindashboard(request):
    return render(request,'admin_dashboard.html')
def Booking(request):
    if request.method == "POST":
          regno =request.POST['regno']
          nameon =request.POST['nameon']
          age=request.POST['age']
          fname = request.POST['fname']
          occ= request.POST['occ']
          mob = request.POST['mob']
          email = request.POST['email']
          stay_period = request.POST['stay_period']
          doj  = request.POST['doj']
          rooms=request.POST['rooms']
          food=request.POST['food']
          ac=request.POST['ac']
          amt = request.POST['amt']
          pay_mode=request.POST['pay_mode']
          PROOF=request.POST['PROOF']
          idnum=request.POST['idnum']
          booking_online.objects.create(
          regno=regno,
          nameon=nameon,
          age=age,
          fname=fname,
          occ=occ,
          mob=mob,
          email=email,
          stay_period=stay_period,
          doj=doj,
          rooms=rooms,
          food=food,
          ac=ac,
          amt=amt,
          pay_mode=pay_mode,
          PROOF=PROOF,
          idnum=idnum)
          return HttpResponse('Booked Successfully!!!')

    return render(request,'Booking.html')
def tariffdetails(request):
    tariff=roomdetails_online.objects.all()
    return render(request,'tariffdetails.html',{'tariff':tariff})

def onlinebooking(request):
    return render(request,'online_bookings.html')
def offlinebooking(request):
    return render(request,'offline_bookings.html')
def rooms(request):
    if request.method == "POST":
        room_type=request.POST['room_type']
        ac_nonac = request.POST['ac_nonac']
        total_rooms = int(request.POST['total_rooms'])
        booked_rooms = int(request.POST['booked_rooms'])
        available_rooms = total_rooms - booked_rooms
        price_per_month = int(request.POST['price_per_month'])
        food_cost = int(request.POST['food_cost'])
        total_price = price_per_month + food_cost

        roomdetails_online.objects.create(
            room_type=room_type,
            ac_nonac=ac_nonac,
            total_rooms=total_rooms,
            booked_rooms=booked_rooms,
            available_rooms=available_rooms,
            price_per_month=price_per_month,
            food_cost=food_cost,
            total_price=total_price

        )
        return redirect('tariffdetails')

    return render(request,'Updating_room_details_online.html')


def updation(request):
    if request.method == "POST":
        try:
            img1 = request.FILES['img1']
            img2 = request.FILES['img2']
            img3 = request.FILES['img3']
            img4 = request.FILES['img4']
            video = request.FILES['video']
        except KeyError as e:
            return HttpResponse(f'Missing file: {e}')

        fs = FileSystemStorage()
        img1_name = fs.save(img1.name, img1)
        img2_name = fs.save(img2.name, img2)
        img3_name = fs.save(img3.name, img3)
        img4_name = fs.save(img4.name, img4)
        video_name = fs.save(video.name, video)

        profile = profile_updation.objects.create(
            img1=img1_name,
            img2=img2_name,
            img3=img3_name,
            img4=img4_name,
            video=video_name
        )

        context = {
            'img1_name': profile.img1.url,
            'img2_name': profile.img2.url,
            'img3_name': profile.img3.url,
            'img4_name': profile.img4.url,
            'video_name': profile.video.url
        }
        return render(request, 'Profile_updation.html', context)
    return render(request, 'Profile_updation.html')

def gallery(request):
    gallery = profile_updation.objects.all()
    return render(request, 'Hostel_Gallery.html', {'gallery': gallery})
def bookeddetails(request):
    booked=booking_online.objects.all()
    return render(request,'Booked_details.html',{'booked':booked})


def offregister(request):
        if request.method == "POST":
            offreg = request.POST['offreg']
            offname = request.POST['offname']
            offage = request.POST['offage']
            father = request.POST['father']
            occupation = request.POST['occupation']
            mobile = request.POST['mobile']
            off_email = request.POST['off_email']
            p_o_stayy = request.POST['p_o_stayy']
            stay_period = request.POST['stay_period']
            date_of_join= request.POST['date_of_join']
            rooms= request.POST['rooms']
            food = request.POST['food']
            ac = request.POST['ac']
            PROOF = request.POST['PROOF']
            idnum = request.POST['idnum']
            amt = request.POST['amt']
            mode = request.POST['mode']


            offline_registration.objects.create(
                offreg=offreg,
                offname=offname,
                offage=offage,
                father=father,
                occupation=occupation,
                mobile=mobile,
                off_email=off_email,
                p_o_stayy=p_o_stayy,
                stay_period=stay_period,
                date_of_join=date_of_join,
                rooms=rooms,
                food=food,
                ac=ac,
                PROOF=PROOF,
                idnum=idnum,
                amt=amt,
                mode=mode,

            )
            return HttpResponse('success')
        return render(request,'offline_registration_form.html')
def roomallotment(request):
    if request.method == "POST":
          roomno =request.POST['roomno']
          client =request.POST['client']
          roomtype =request.POST['roomtype']
          roomnature=request.POST['roomnature']

          room_allotment.objects.create(
          roomno=roomno,
          client=client,
          roomtype=roomtype,
          roomnature=roomnature)
          return HttpResponse('success')
    return render(request,'ROOM_ALLOTMENT.html')
def management(request):
    if request.method == "POST":
        things=request.POST['things']
        number_of_items = request.POST['number_of_items']
        room_num = request.POST['room_num']
        collection = request.POST['collection']
        expenses= request.POST['expenses']
        income = request.POST['income']
        inventory.objects.create(
            things=things,
            number_of_items=number_of_items,
            room_num=room_num)
        accounts.objects.create(
            collection=collection,
            expenses=expenses,
            income = income)
        return redirect('managementdetails')
    return render(request,'management.html')
def managementdetails(request):
    management = inventory.objects.all()
    account = accounts.objects.all()
    return render(request,'management_details.html',{
        'management':management,
        'account':account
    })
def off_reg_det(request):
    offline=offline_registration.objects.all()
    return render(request,'off_reg_det.html',{'offline':offline})

