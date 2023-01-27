from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import requests,json
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
# from .models import Role, RoleCategory
# from .forms import RoleForm
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
# from accounts.models import Role
from django.contrib.auth. forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.http import HttpResponse
import requests,json,http.client,ssl

def login(request):
    return render(request,'login.html')
def testing(request):
    return render(request,'selection.html')
# def weather(request):
#     return render(request,'weather.html')

