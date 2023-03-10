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
        electricity_monthly = request.POST.get('electricity_monthly')
        distance_petrol = request.POST.get('distance_petrol')
        distance_disel = request.POST.get('distance_disel')
        lpg = request.POST.get('lpg')

        print(electricity_monthly,distance_petrol,distance_disel,lpg)
        
    return render(request, 'cc_car.html')



def cc_output(request):
    return render(request, 'cc_output.html')




def cc_industry(request):
    return render(request, 'cc_industry.html')



# Electricity_yearly = Electricity_monthly*12
# Electricity_yearly_emission = Electricity_yearly*0.85
# Pertrol_Km = Yearly_distance_travelled_petrol/10
# Petrol_Emission = Pertrol_Km*2.296
# Diesel_Km = Yearly_distance_travelled_diesel/12
# Diesel_Emission = Diesel_Km*2.653
# LPG_yearly_Emission = LPG_qty * 2.983
# Carbon_Footprint = (Electricity_yearly_emission + Petrol_Emission + Diesel_Emission + LPG_yearly_Emission)/1000