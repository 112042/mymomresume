import requests
from isodate import parse_duration
from django.conf import settings
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse   #基本的伺服器回復
from django.http import HttpResponseRedirect   #伺服器的路徑進行重定向
from django.contrib import auth              #導入Django內建認證函數
from django.contrib.auth.decorators import login_required              #導入Django login_requirement
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
#from django.contrib.auth.models import User, Group
from json import dumps

# Create your views here.

def index(request):
    return render(request,'index.html')

def care(request):
    return render(request,'care.html')

def child(request):
    return render(request,'child.html')

def contact(request):
    return render(request,'contact.html')

def confinement(request):
    return render(request,'confinement.html')