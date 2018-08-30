from django.shortcuts import render,HttpResponse, redirect
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import json
import datetime
dt_format = '%m/%d/%Y'

def index(request):
    return render(request,'fconn_app/index.html')

def signin(request):
    if request.method == "POST":
        reg_form = RegistrationForm(data=request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            user.set_password(user.password)
            user.save()
            request.session['username'] = user.username
            return redirect('/dashboard')
        else:
            print(reg_form.errors)
    else:
        reg_form = RegistrationForm()
    return render(request,'fconn_app/signin.html',{'registration_form': reg_form})


def logval(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                request.session['username'] = username
                return redirect('/dashboard')
            else:
                print("user is not active")
        else:
            messages.error(request,"Bad Credentials!",extra_tags='login')
            return redirect('/signin')

def profile(request):
        user = User.objects.get(username=request.session['username'])
        users = UserProfileInfo.objects.filter(user_id = user.id)
        if users.count() > 0 :
            return render(request,'fconn_app/profile.html',{'user':user,'userProfile': users[0]})
        else:
            return render(request,'fconn_app/profile.html',{'user':user})


def userInfoVal(request):
    if request.method == "POST":
        b = User.objects.get(username=request.session['username'])
        b.firstName = request.POST['firstName']
        b.lastName = request.POST['lastName']
        b.save()
            # b.email = request.POST['email']atetime.datetime.strptime(d1, dt_format)
        u = UserProfileInfo.objects.filter(user_id = b.id)
        if u.count() > 0 :
            u[0].user_id = b.id
            u[0].birthday = request.POST['birthday']
            u[0].address = request.POST['address']
            u[0].city = request.POST['city']
            u[0].state = request.POST['state']
            u[0].schoolState = request.POST['schoolState']
            u[0].major =   request.POST['major']
            u[0].schoolName = request.POST['schoolName']
            u[0].gender = request.POST["gender"]
            b.save()
        else:
            UserProfileInfo.objects.create(user_id = b.id,birthday = request.POST['birthday'],address=request.POST['address'],city=request.POST['city'],state=request.POST['state'],schoolState=request.POST['schoolState'],major=request.POST['major'],schoolName=request.POST['schoolName'],gender=request.POST['gender'])
        return redirect('/dashboard')
    else:
        return render(request,'fconn_app/profile.html')

def dashboard(request):
    userColleges = {}
    username = request.session['username']
    allColleges = College.objects.all()
    user = User.objects.get(username = username)
    user_colleges = College.objects.filter(user = user)
    if user_colleges.count() > 0 :
    # checklist = Checklist.objects.filter(user = user)
        return render(request,'fconn_app/dashboard.html',{'user':user, "colleges": allColleges,"user_colleges" : user_colleges})
    else:
        return render(request,'fconn_app/dashboard.html',{'user':user, "colleges": allColleges})



def addCollege(request):
    user = User.objects.get(username=request.session['username'])
    newcollege = College.objects.get(id=request.POST['college'])
    m1 = Checklist(student = user,college=newcollege)
    m1.save()
    return redirect('/dashboard')

def checklist(request,number):
    college = College.objects.get(id=number)
    user = User.objects.get(username=request.session['username'])
    checklist = Checklist.objects.get(college = college,student = user)
    print(checklist.application)
    return render(request,'fconn_app/checklist.html',{'college':college,'checklist':checklist})
            # user =
            #
            #
            # checklist = checklist_form.save(commit=False)
            # checklist.save()
        # checklist_form = ChecklistForm()
def updatechecklist(request,number):
    college = College.objects.get(id=number)
    user = User.objects.get(username=request.session['username'])
    checklist = Checklist.objects.get(college = college,student = user)
    checklist.application = request.POST['application']
    checklist.test_scores = request.POST['test_scores']
    checklist.school_transcript = request.POST['school_transcript']
    checklist.reports = request.POST['reports']
    checklist.sec_school_reports = request.POST['sec_school_reports']
    checklist.recommenadtion = request.POST['recommendation']
    checklist.save()
    return redirect('/dashboard')

def resources(request):
    allResources = Resource.objects.all()
    return render(request,'fconn_app/resource.html',{'resources':allResources})

def logout(request):
    request.session.flush()
    return redirect('/')
