from django.shortcuts import render, redirect
from math import ceil
from django.http import HttpResponse
from .models import HostelDetail, StudentDetaile, login

from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def studentDetaile(request):
    if request.method == "POST":
        student_name = request.POST.get('student_name', '')
        enroll_no = request.POST.get('enroll_no', '')
        course = request.POST.get('course', '')
        dob = request.POST.get('dob', '')
        add_yr = request.POST.get('add_yr', '')
        dept_name = request.POST.get('dept_name', '')
        email_id = request.POST.get('email_id', '80')
        phone_no = request.POST.get('phone_no', '')
        # image = request.POST.get('image', '')
        # bed_no = request.POST.get(' bed_no', '')
        gender = request.POST.get('gender', '')
        hostel_name = request.POST.get('hostel_name', '')
        room_no = request.POST.get('room_no', '')
    
        hostels = HostelDetail.objects.all()
        detail = StudentDetaile.objects.filter(hostel_name=hostel_name).values("hostel_name", "room_no", "h_id")
        if detail:
            print("<<<<<<<<<<<if>>>>>>>>>>>>>>>>>>>")
    
            for hostel in hostels:
                for i in detail:
                    if i["room_no"] == int(room_no) and hostel.name == hostel_name:
                        student = StudentDetaile(student_name=student_name,
                                                 enroll_no=enroll_no,
                                                 course=course,
                                                 dob=dob,
                                                 add_yr=add_yr,
                                                 dept_name=dept_name,
                                                 email_id=email_id,
                                                 phone_no=phone_no,
                                                 # image=image,
                                                 # bed_no=bed_no,
                                                 gender=gender,
                                                 hostel_name=hostel_name,
                                                 room_no=room_no,
                                                 h_id=hostel)
                        
                        if hostel.vacancy < hostel.capacity:
                            # ye kya kr rhe ho
                            HostelDetail.objects.filter(id=hostel.id).update(vacancy=hostel.vacancy  +1)
                            # hostel.vacancy  += 1
                            # hostel.vacancy.save()
                            student.save()
                            print("<<<<<<<<<<<save>>>>>>>>>>>>>>>>>>>")

                            return render(request, 'studentDetaile.html', {"data": "Detailes are submitted"})
                        else:
                            print("<<<<<<<<<<else  save tata full>>>>>>>>>>>>>>>>>>>")
                            return render(request, 'studentDetaile.html',{"data":"These Room Are Not Vacant"})
                        # return render(request, 'studentDetaile.html', {"data": "hnotpres,rom alr pre"})
                    # return render(request, 'studentDetaile.html',{"data":"hnotpres,rom alr pre"})

                # return render(request, 'studentDetaile.html',{"data":"hnotpres,rom alr pre"})
            return render(request, 'studentDetaile.html',{"data":"Hostel Not Present and also Room are Not Present.."})
        else:
            hostel = HostelDetail.objects.all()
            print(">>>>>>>>>>>else>>>>>>>>>")
            for i in hostel:
                print(">>>>>>>>>>>else> iiiii>>>>>>>>")
    
                if i.name == hostel_name:
                    print(">>>>>>>>>>>else>hhkhbhjbj>>>>>>>>")
    
                    student = StudentDetaile(student_name=student_name,
                                             enroll_no=enroll_no,
                                             course=course,
                                             dob=dob,
                                             add_yr=add_yr,
                                             dept_name=dept_name,
                                             email_id=email_id,
                                             phone_no=phone_no,
                                             # image=image,
                                             # bed_no=bed_no,
                                             gender=gender,
                                             hostel_name=hostel_name,
                                             room_no=room_no,
                                             h_id=i)
                    HostelDetail.objects.filter(id=i.id).update(vacancy=i.vacancy + 1)
                    student.save()
                    print("save student data")
                    return render(request, 'studentDetaile.html', {"data":"Detailes are submitted. "})
                # return render(request, 'studentDetaile.html', {"data": "Hostel are not present"})
        return render(request, 'studentDetaile.html')
    return render(request, 'studentDetaile.html')



def vacant(request):
    students = HostelDetail.objects.all().values("name","rooms", "capacity","vacancy")
    l = []
    for i in students:
        if i["capacity"]> i["vacancy"]:
            l.append({"name": i["name"],
                      "rooms": i["rooms"],
                      "capacity": i["capacity"],
                      "vacancy": i["vacancy"]})
    return render(request, 'vacant.html', {"students":l})


def nmhVacant(request):
    students = HostelDetail.objects.all().values("name","rooms", "capacity","vacancy")
    l = []
    for i in students:
        print(">>>>>>>>>>")
        if i["capacity"]> i["vacancy"] and i["name"]=="NILACHAL MENS HOSTEL":
            l.append({"rooms": i["rooms"],
                      "capacity": i["capacity"],
                      "vacancy": i["vacancy"]})
    return render(request, 'nmhVacant.html', {"students":l})



def nmhDetaile(request):
    students = StudentDetaile.objects.all().values("student_name","enroll_no", "course", "dob","add_yr","dept_name",
                                                   "email_id","phone_no","gender","hostel_name","room_no")
    l = []
    for i in students:
        # if i["hostel_name"]=="NILACHAL MENS HOSTEL":
        l.append({"student_name": i["student_name"],
                      "enroll_no":i["enroll_no"],
                      "course":i["course"],
                      "dob":i["dob"],
                      "add_yr":i["add_yr"],
                      "dept_name":i["dept_name"],
                      "email_id":i["email_id"],
                      "phone_no":i["phone_no"],
                      "gender":i["gender"],
                      "hostel_name":i["hostel_name"],
                      "room_no":i["room_no"]})
    return render(request, 'nmhDetaile.html', {'students':l})
    # return render(request, 'nmhDetaile.html')


# status=False
def hostel_details(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        rooms = request.POST.get('rooms', '')
        capacity = request.POST.get('capacity', '')

        hostel=HostelDetail(name=name,
                            rooms=rooms,
                            capacity=capacity)
        hostel.save()
    # return render(request, 'hostel_details.html', status="Submit")

    return render(request, 'hostel_details.html')

#
def add(request):
        return render(request, 'add.html')


def besic(request):
    return render(request, 'besic.html')


def add_nmh(request):
    return render(request, 'add_nmh.html')


def NMH(request):
    return render(request, 'NMH.html')
def PMH(request):
    return render(request, 'PMH.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def loginW(request):
    if request.method == "POST":
        # hostel_name = request.POST.get('hostel_name', '')
        user_name = request.POST.get('user_name', '')
        wpassword = request.POST.get('wpassword', '')
        if user_name== 'nmh' and wpassword== 'nmh@123':
            return render(request, 'nmhW.html')
            
        if user_name== 'pmh' and wpassword== 'pmh@123':
            return render(request, 'PMH.html')
        
        if user_name == 'kmh' and wpassword == 'kmh@123':
            return render(request, 'KMH.html')

        if user_name == 'cmh' and wpassword == 'cmh@123':
            return render(request, 'CMH.html')
        
        if user_name == 'tmh' and wpassword == 'tmh@123':
            return render(request, 'KMH.html')

        if user_name == 'cmh' and wpassword == 'cmh@123':
            return render(request, 'CMH.html')
        
        if user_name == 'twh' and wpassword == 'twh@123':
            return render(request, 'TWH.html')

        if user_name == 'nwh' and wpassword == 'nwh@123':
            return render(request, 'NWH.html')
        
        if user_name == 'pwh' and wpassword == 'pwh@123':
            return render(request, 'PWH.html')

        if user_name == 'swh' and wpassword == 'swh@123':
            return render(request, 'SWH.html')

    return render(request, 'loginW.html')

def loginA(request):
    if request.method == "POST":
        au_name = request.POST.get('au_name', '')
        apassword = request.POST.get('apassword', '')
        if au_name =='Admin' and apassword=='admin@123':
            return render(request, 'index.html')
        else:
            return render(request, 'loginA.html', {"data":"Wrong User Name Or Password..."})

    return render(request, 'loginA.html')

def loginS(request):
    return render(request, 'loginS.html')

def admini_Login(request):
    return render(request, 'admini_Login.html')

def show_Hdetaile(request):
    students = HostelDetail.objects.all().values("name", "rooms","capacity","vacancy")
    
    l = []
    for i in students:
        # h = {}
        # h["h_name"] = i["name"]
        # h["room"] = i["rooms"]
        # l.append(h)
        l.append({"name":i["name"],"rooms":i["rooms"],"capacity":i["capacity"],"vacancy":i["vacancy"]})
    # print(l,"??????????????")
    return render(request, 'show_Hdetaile.html',{'students':l} )


def show_Sdetaile(request):
    students = StudentDetaile.objects.all().values("student_name","enroll_no", "course", "dob","add_yr","dept_name",
                                                   "email_id","phone_no","gender","hostel_name","room_no")
    l = []
    for i in students:
        l.append({"student_name": i["student_name"],
                  "enroll_no":i["enroll_no"],
                  "course":i["course"],
                  "dob":i["dob"],
                  "add_yr":i["add_yr"],
                  "dept_name":i["dept_name"],
                  "email_id":i["email_id"],
                  "phone_no":i["phone_no"],
                  "gender":i["gender"],
                  "hostel_name":i["hostel_name"],
                  "room_no":i["room_no"]})
    return render(request, 'show_Sdetaile.html', {'students':l})

def search(request):
    if request.method =='POST':
        book_name = request.POST['search']
        if book_name:
            student = StudentDetaile.objects.filter(Q(student_name__icontains=book_name) |
                                                  Q(enroll_no__icontains=book_name) |
                                                  Q(room_no__icontains=book_name))
            if student:
                return render(request, 'search.html', {'books':student})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponse('/search/')

    return render(request, 'search.html')
#
def KMH(request):
    return render(request, 'KMH.html')
    
def delete(request):
    if request.method == 'POST':
        data = StudentDetaile.objects.all()
        item_id = int(request.POST.get('item_id'))
        item = StudentDetaile.objects.get(id=item_id)
        item.delete()
    # query = StudentDetaile.objects.get(pk=str(id))
    # query.delete()
        return HttpResponse("Deleted!")
    # # return render(request, 'delete.html')