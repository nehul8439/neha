from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
	path('',Enter),
	path('service',service),
	path('designer',designer),
	path('package',package),
	path('contact',contact),
	path('login',login),
	path('register',register),
	path('signup',signup),
]
