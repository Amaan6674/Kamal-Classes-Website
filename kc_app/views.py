from django.shortcuts import render,redirect
from kc_project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import FeedModel

def home(request):
		return render(request,'home.html')

def acheivements(request):
		return render(request,'acheivements.html')

def courses(request):
		return render(request,'courses.html')

def centers(request):
		return render(request,'centers.html')

def feedback(request):
	if request.method=="POST":
		e="asgroup693@gmail.com"
		n=request.POST.get("name")
		clg=request.POST.get("clg")
		phone=request.POST.get("phone")
		feed=request.POST.get("message")
		ff=FeedModel.objects.create(name=n,clg=clg,phone=phone,message=feed)
		ff.save()
		send_mail("FeedBack From Your User","Name:"+n+"\nCollege/Company:"+clg+"\nPhone:"+phone+"\nMessage:"+feed,EMAIL_HOST_USER,[e])
		return render(request,'feedback.html',{'msg':'Will get back to you soon'})
	else:
		return render(request,'feedback.html')
		
		
