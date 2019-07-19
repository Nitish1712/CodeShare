from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Coder
from django.contrib.auth import login,logout
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.sessions.models import Session
# Create your views here.
def home_view0(request):
	return render(request,"home_page.html",{'Users':Coder.objects.all(),'coder':None})

def home_view1(request,name):
	user = User.objects.get(username=name)
	coder = Coder.objects.get(user=user)
	return render(request,"home_page.html",{'Users':Coder.objects.all(),'coder':coder})

def signup_view(request):
	if(request.method == 'POST'):
		form = UserCreationForm(request.POST)
		if form.is_valid() :
			user = form.save()
			a = Coder()
			a.user = user
			a.save()
			login(request,user)
			return redirect('/')
	else:
		form = UserCreationForm()
	return render(request,"signup.html",{'form':form})

def logout_view(request):
	logout(request)
	return redirect('/')

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data = request.POST)
		f=0
		if form.is_valid():
			my_old_sessions = Session.objects.all()
			for row in my_old_sessions:
			    uid = row.get_decoded().get("_auth_user_id") 
			    cid =  User.objects.get(username = form.get_user()).pk
			    if uid is not None and int(uid) == int(cid) :
			    	f=1
			print(f)
			if f==0:
				login(request,form.get_user())
			return redirect('/')
	else:
		form = AuthenticationForm(None,request.POST)
	return render(request,"login.html",{'form':form})

def modify_view(request):
	try:
		code = request.GET.get('code',None)
		coder = Coder.objects.get(user=request.user)
		coder.code = code
		coder.save()
		data={
			'done': True
		}
	except:
		data = {
			'done' : False
		}
	return JsonResponse(data)

def initialise(request):
	try:
		coder = Coder.objects.get(user=request.user)
		data={
			'code': coder.code
		}
	except:
		data = {
			'code' : "COULDN'T LOAD :( "
		}
	return JsonResponse(data)

def update_view(request):
	try:
		name = request.GET.get('name',None)
		coder = Coder.objects.get(user=User.objects.get(username=name))
		data={
			'code': coder.code
		}
	except:
		data = {
			'code' : "COULDN'T LOAD :( "
		}
	return JsonResponse(data)