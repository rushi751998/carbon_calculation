from django.shortcuts import render, HttpResponse, redirect
from .forms import Calculator_form


def index(request):
    return render(request, 'index.html')


def cc(request):
    return render(request, 'cc.html')

def family_carbon_calculator(Electricity_monthly,Yearly_distance_travelled_petrol,Yearly_distance_travelled_diesel,LPG_qty):
    Electricity_yearly = Electricity_monthly*12
    Electricity_yearly_emission = Electricity_yearly*0.85
    Pertrol_Km = Yearly_distance_travelled_petrol/10
    Petrol_Emission = Pertrol_Km*2.296
    Diesel_Km = Yearly_distance_travelled_diesel/12
    Diesel_Emission = Diesel_Km*2.653
    LPG_yearly_Emission = LPG_qty * 2.983
    Carbon_Footprint = (Electricity_yearly_emission + Petrol_Emission + Diesel_Emission + LPG_yearly_Emission)/1000

    return Carbon_Footprint

ls = []
def cc_home(request):
    parm = {"form":Calculator_form()}
    return render(request, 'cc_home.html',parm)


def cc_result(request):
    if request.method =="POST": 
        electricity_monthly = int(request.POST.get('electricity_monthly'))
        Yearly_distance_travelled_petrol = int(request.POST.get('distance_petrol'))
        Yearly_distance_travelled_diesel = int(request.POST.get('distance_disel'))
        LPG_qty = int(request.POST.get('lpg'))
        cc_house =family_carbon_calculator(electricity_monthly,Yearly_distance_travelled_petrol,Yearly_distance_travelled_diesel,LPG_qty)
        ls.append(cc_house)
        parm = {"calulations":round(cc_house,2)}    
        return render(request, 'result.html',parm)

def cc_car(request):

        return render(request, 'cc_car.html')



def cc_output(request):
    param = {'results':round(sum(ls),2)}
    return render(request, 'cc_output.html' ,param)




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