from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from models import Order
from datetime import *
from django.http import HttpResponse
from django.db.models import Sum
import json
import calendar
from django.utils import timezone

# Create your views here.

def index_main(request):
    return render(request, 'index_main.html')


def myinfo(request):
    return render(request, 'myinfo.html')


def login_main(request):
    if request.method == "GET":
        form = AuthenticationForm

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(to="index_website")

    context = {}
    context['form'] = form

    return render(request, 'login_main.html', context)


def register(request):
    if request.method == "GET":
        form = UserCreationForm

    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='login')

    context = {}
    context['form'] = form

    return render(request, 'register.html', context)


def get_today_money(request):
    now = timezone.now()
    day_start = datetime(now.year, now.month, now.day, 0, 0, 0, 0)
    day_end = datetime(now.year, now.month, now.day, 23, 59, 59, 999999)
    res = Order.objects.filter(finish_time__gt=day_start, finish_time__lte=day_end).aggregate(Sum('fee'))
    fee = res['fee__sum']
    if not fee:
        fee = 0
    result = {'fee': fee}
    return HttpResponse(json.dumps(result), content_type="application/json")


def get_current_month_money(request):
    now = timezone.now()
    monthRange = calendar.monthrange(now.year, now.month)
    month_start = datetime(now.year, now.month, 1, 0, 0, 0, 0)
    month_end = datetime(now.year, now.month, monthRange[-1], 23, 59, 59, 999999)
    res = Order.objects.filter(finish_time__gt=month_start, finish_time__lte=month_end).aggregate(Sum('fee'))
    fee = res['fee__sum']
    if not fee:
        fee = 0
    result = {'fee': fee}
    return HttpResponse(json.dumps(result), content_type="application/json")