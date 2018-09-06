from django.shortcuts import render
from myapp.forms import *
from myapp.models import *
from fulldesign import settings
from django.contrib import messages,auth
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth import logout
# Create your views here.
def Enter(request):
	return render(request,"index.html")
	
def service(request):
	return render(request,"service.html")
	
	
def designer(request):
	return render(request,"designer.html")
	
	
def package(request):
	return render(request,"package.html")
	
def contact(request):
	return render(request,"contact.html")
	

	
	
def login(request):
    if request.method == 'POST':
        user_name = request.POST['user']
        passw = request.POST['password']

        try:
            user = auth.authenticate(username=user_name, password=passw)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/slist/')
            else:
                messages.error(request, "invalid")
        except:
            messages.error(request, 'Invalid User')

    return render(request, 'login.html')


	
def register(request):
    if(request.method=='POST'):
        form=Fulldesign_form(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            messages.success(request,"Servant Registered Successfully")
            return HttpResponseRedirect('/register/')
        else:
            messages.error(request,"Invalid form")
    else:
        form=Fulldesign_form()
    return render(request,'register.html')

	


	
	
def signup(request):
    if (request.method == 'POST'):
        form = Fulldesign_form(request.POST)
        if (form.is_valid()):
            form.save()
            messages.success(request, "User Registered Successfully")
            return HttpResponseRedirect('/sign_up/')
        else:
            messages.error(request, "Invalid form")
    else:
        form = Fulldesign_form()
    return render(request, 'signup.html')
