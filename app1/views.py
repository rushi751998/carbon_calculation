from django.shortcuts import render, HttpResponse, redirect
from .forms import Calculator_form
import pandas as pd


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
        form = Calculator_form(request.GET)
        try :
            electricity_monthly = int(request.POST.get('electricity_monthly'))
            form = Calculator_form(request.GET)
            Yearly_distance_travelled_petrol = int(request.POST.get('distance_petrol'))
            Yearly_distance_travelled_diesel = int(request.POST.get('distance_disel'))
            LPG_qty = int(request.POST.get('lpg'))
            cc_house =family_carbon_calculator(electricity_monthly,Yearly_distance_travelled_petrol,Yearly_distance_travelled_diesel,LPG_qty)
            ls.append(cc_house)
            parm = {"calulations":round(cc_house,2)}    
            return render(request, 'result.html',parm)
        except:
            return render(request, 'cc_home.html',{"form":Calculator_form(),'error':'Please Fill all the Parameter'})


def cc_car(request):

        return render(request, 'cc_car.html')



def cc_output(request):
    param = {'results':round(sum(ls),2)}
    return render(request, 'cc_output.html' ,param)




def cc_industry(request):
    param = {
    'admimistratation':('Electricity_yearly_emission' , 'WaterWaste_Yearly_emission','Solidwaste_yearly_emission','GeneratorGrid_Yearly_emission','GeneratorDiesel_Yearly_emission'),
    "transport" :['Bus_yearly_emission','Car_Yearly_emission','Bike125_Yearly_emission','Bike500_Yearly_emission'],
    'Appliances':('Desktop_Yearly_emission','SmartPhone_Yearly_emission','Print_Yearly_emission','Laptop_Yearly_emission','Projector_Yearly_emission')
     }

   
    return render(request, 'industry_result.html',param)

def cc_result_industry(request):
    param  = {}
        
    return render(request, 'industry_resul.html',param)


def get_trend_df():
    raw = pd.read_csv('raw.csv')
    forcasted = pd.read_csv('foracsed.csv')
    return raw,forcasted


def trend(request):
    raw ,forcasted =get_trend_df()
    filtered =raw[(raw['Country']=='Australia')& (raw['Pollutant']=='Carbon dioxide')&(raw['Variable'] =='Total  emissions excluding LULUCF')][['Year','Value']]
    forcasted =forcasted[(forcasted['Country']=='Australia')& (forcasted['Pollutant']=='Carbon dioxide')&(forcasted['Variable'] =='Total  emissions excluding LULUCF')][['YEA','Forecast']] 
    # print(forcasted)
    # if request.method == "POST":
    #     region = request.POST.get('region')
    #     country = request.POST.get('country')
    #     pollutant = request.POST.get('pollutants')
    #     # print(region)
    #     # print(country)
    #     # print(pollutant)
    #     year = raw['Year'].unique()
    #     filtered =raw[(raw['Country']==country)& (raw['Pollutant']==pollutant)&(raw['Variable'] =='Total  emissions excluding LULUCF')][['Year','Value']] 
    
    param = {
        'region':raw['COU'].unique(),
        'country':raw['Country'].unique(),
        'pollutant':raw['Pollutant'].unique(),
        # 'year':[1,2,3,4],
        # 'co2':[65,23,65,23]
        'year':filtered['Year'].values,
        'co2':filtered['Value'].values,
        'forcasted_year':forcasted['YEA'].values,
        'forcasted_co2':forcasted['Forecast'].values ,
    }

    return render(request, 'trend.html',param)


def forcasted_trend(request):
    raw ,forcasted =get_trend_df()
    filtered =raw[(raw['Country']=='Australia')& (raw['Pollutant']=='Carbon dioxide')&(raw['Variable'] =='Total  emissions excluding LULUCF')][['Year','Value']]
    forcasted =forcasted[(forcasted['Country']=='Australia')& (forcasted['Pollutant']=='Carbon dioxide')&(forcasted['Variable'] =='Total  emissions excluding LULUCF')][['YEA','Forecast']] 
    # print(forcasted)
    if request.method == "POST":
        region = request.POST.get('region')
        country = request.POST.get('country')
        pollutant = request.POST.get('pollutants')

        year = raw['Year'].unique()
        filtered =raw[(raw['Country']==country)& (raw['Pollutant']==pollutant)&(raw['Variable'] =='Total  emissions excluding LULUCF')][['Year','Value']] 
        # print(filtered)

    param = {

        'year':filtered['Year'].values,
        'co2':filtered['Value'].values,
        'forcasted_year':forcasted['YEA'].values,
        'forcasted_co2':forcasted['Forecast'].values ,
    }

    return render(request, 'forcasted_trend.html',param)


# Electricity_yearly = Electricity_monthly*12
# Electricity_yearly_emission = Electricity_yearly*0.85
# Pertrol_Km = Yearly_distance_travelled_petrol/10
# Petrol_Emission = Pertrol_Km*2.296
# Diesel_Km = Yearly_distance_travelled_diesel/12
# Diesel_Emission = Diesel_Km*2.653
# LPG_yearly_Emission = LPG_qty * 2.983
# Carbon_Footprint = (Electricity_yearly_emission + Petrol_Emission + Diesel_Emission + LPG_yearly_Emission)/1000

def Industrial_carbon_calculator(Electricity_yearly,WaterWaste_Yearly,SolidWaste_Yearly,Bus_Yearly,car_Yearly,Bike125_Yearly,Bike500_Yearly,Desktop_Count,SmartPhone_Count,Print_Yearly,Laptop_Yearly,GeneratorGrid_Yearly,GeneratorDiesel_Yearly,LPG_qty,Projector_Yearly):
    #Administration
    Electricity_yearly_emission = Electricity_yearly*0.00085
    WaterWaste_Yearly_emission=WaterWaste_Yearly*0.000298
    Solidwaste_yearly_emission=SolidWaste_Yearly*0.000165
    GeneratorGrid_Yearly_emission=GeneratorGrid_Yearly*0.37
    GeneratorDiesel_Yearly_emission=GeneratorDiesel_Yearly*0.79
    LPG_yearly_Emission = LPG_qty * 0.002983
    #Transport
    Bus_yearly_emission=Bus_Yearly*0.000096
    Car_Yearly_emission=car_Yearly*0.000149
    Bike125_Yearly_emission=Bike125_Yearly*0.0001
    Bike500_Yearly_emission=Bike500_Yearly*0.00013237
    #Appliances
    Desktop_Yearly_emission=Desktop_Count*0.778
    SmartPhone_Yearly_emission=SmartPhone_Count*0.063
    Print_Yearly_emission=Print_Yearly*0.000001027
    Laptop_Yearly_emission=Laptop_Yearly*0.10562
    Projector_Yearly_emission=Projector_Yearly*0.001
    Carbon_Footprint=(Electricity_yearly_emission + WaterWaste_Yearly_emission + Solidwaste_yearly_emission 
                        + Bus_yearly_emission + Car_Yearly_emission + Bike125_Yearly_emission 
                        + Bike500_Yearly_emission + Desktop_Yearly_emission + SmartPhone_Yearly_emission 
                        + Print_Yearly_emission +Laptop_Yearly_emission + GeneratorGrid_Yearly_emission 
                        + GeneratorDiesel_Yearly_emission+LPG_yearly_Emission + Projector_Yearly_emission)
    return Carbon_Footprint