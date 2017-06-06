from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from counter.models import RoomCall, UserRoom
from website.forms import ReserveForm

# Create your views here.


def index_website(request):
    return render(request, 'index_website.html')

def reserve_website(request):
    if request.method == 'GET':
        form = ReserveForm
        context = {}
        context['form'] = form
        return render(request, 'reserve_website.html', context)
    else:
        user_name = request.POST.get('name', '')
        user_phone = request.POST.get('phone', '')
        room_number = request.POST.get('room_number', '')
        start_time = request.POST.get('start_time', '')
        end_time = request.POST.get('end_time', '')
        user_room = UserRoom()
        user_room.user_name = user_name
        user_room.user_phone = int(user_phone)
        user_room.room_number = int(room_number)
        user_room.start_time = str(start_time)
        user_room.end_time = str(end_time)
        user_room.save()
        return redirect(to="index_customer")


def search_website(request):
    return render(request, 'search_website.html')

def selectsong_website(request):
    return render(request, 'selectsong_website.html')

def callbar_website(request):
    if request.method == "POST":
        room_number = request.POST.get('room_number', 0)
        if room_number > 0:
            room_number = int(room_number)
            room_call = RoomCall()
            room_call.room_number = room_number
            room_call.call_time = datetime.now()
            room_call.save()
        return HttpResponse()

    return render(request, 'callbar_website.html')
