from django.shortcuts import render, HttpResponse, redirect
from .forms import Calculator_form


def index(request):
    return render(request, 'index.html')


def cc(request):
    return render(request, 'cc.html')


def cc_home(request):
    parm = {"form":Calculator_form()}
    return render(request, 'cc_home.html',parm)

def cc_car(request):
    if request.method =="POST":
        form_responce = request.POST.get('abc')

        print((form_responce))
        
    return render(request, 'cc_car.html')



def cc_output(request):
    return render(request, 'cc_output.html')




def cc_industry(request):
    return render(request, 'cc_industry.html')