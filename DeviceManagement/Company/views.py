from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Company
from .models import Employees
# Create your views here.

def home(request):
    return render(request,"Home.html")


def employee_list(request):
    employees = Employees.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def register(request):
    form=UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data.get("username")
      messages.success(request, f'your account was created Successfully')
      a=Company.objects.create(name=username)
      a.save()
      return redirect('home')
    context = {
        'form':form  
    } 
    return render(request, "register.html", context)

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

