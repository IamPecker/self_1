from django.shortcuts import render

# Create your views here.


def index_counter(request):
    return render(request,'index_counter.html')
