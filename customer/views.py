from django.shortcuts import render

# Create your views here.


def index_customer(request):
    return render(request,'index_customer.html')
