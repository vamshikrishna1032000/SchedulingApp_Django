from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Course, Student, Tutor, Assignment
from django.utils import timezone
from datetime import date

# Create your views here.

def index(request):
    return render(request,"login.html")

def user_login(request):
    if request.method=="POST":
        username= request.POST['username']
        pasw= request.POST['pasw']

        user = authenticate(request, username=username, password=pasw)
        if user is not None:
            login(request, user)
            return redirect(user_home)
    
        else:
            messages.error(request,"Username or password invalid")
            return redirect('login.html')

    return render(request,"login.html")

def user_home(request):
    current_user = request.user
    today=date.today()
    
    try:
        student = current_user.student
        todaysessions = Assignment.objects.filter(student__sid=student, date=today)
        upcsessions = Assignment.objects.filter(student__sid=student, date__gt=today)
    except Student.DoesNotExist:
        todaysessions = []
        upcsessions = []

    try:
        tutor = current_user.tutor
        todaytutsessions = Assignment.objects.filter(tutor__tid=tutor, date=today)
        upctutsessions = Assignment.objects.filter(tutor__tid=tutor, date__gt=today)
    except Tutor.DoesNotExist:
        todaytutsessions = []
        upctutsessions = []
    return render(request,"home.html",{'tsessions':todaysessions,'upsessions':upcsessions, 'ttutsessions':todaytutsessions,'uptutsessions':upctutsessions})

def user_logout(request):
    logout(request)
    messages.success(request,"Logged out")
    return render(request,"login.html")

def register(request):

    if request.method=="POST":
        username= request.POST['username']
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        email= request.POST['email']
        pasw1= request.POST['pasw1']
        pasw2= request.POST['pasw2']
        if(pasw1!=pasw2):
            messages.error(request,"Passwords dont match")
            return redirect('login.html')
        theuser = User.objects.create_user(username,email,pasw1)
        theuser.first_name = firstname
        theuser.last_name = lastname

        theuser.save()
        messages.success(request,"Registered successfully")
        return redirect('login.html')
    
    return render(request,"register.html")

def forgotpasw(request):
    if request.method=="POST":
        messages.success(request,"Please check your email")
        return redirect('login.html')
    return render(request,"forgotpasw.html")

def addsession(request):
    c=Course.objects.all()
    if request.method=="POST":
        coursecode= request.POST['dropdown']
        t=Tutor.objects.filter(course_code=coursecode)
        return render(request,"addsession.html",{'courses':c,'tuts':t,'selcourse':coursecode})
        
    return render(request,"addsession.html",{'courses':c})

def check_avail(request):
    c=Course.objects.all()
    if request.method=="POST":
        selctutor= request.POST['dropdownt']
        example= User.objects.get(last_name=selctutor)
        t= Tutor.objects.get(tid=example)
        st=Assignment.objects.filter(tutor=t, student__isnull=True)
        return render(request,"addsession.html",{'avs':st, 'selc': selctutor, 'tut': t, 'courses':c})
    return render(request,"addsession.html")

def add_assignment(request):
    if request.method=="POST":
        assignment_id = request.POST['assignment']
        assignment = Assignment.objects.get(pk=assignment_id)
        student = request.user.student
        assignment.student = student
        assignment.save()
        return render(request,"home.html")
    return render(request,"addsession.html")





def display_tutors(request):
    return render(request,"available_tutors.html")

def availability(request):
    if request.method=="POST":
        tut = Tutor.objects.get(tid=request.user)
        date_avail= request.POST['date_avail']
        p = Assignment(tutor=tut, date=date_avail)
        p.save()
        messages.success(request,"Date added")
        return render(request,"availability.html")
    return render(request,"availability.html")

def test(request):
    return render(request,"test.html")

def testdash(request):
    return render(request,"testdashboard.html")
