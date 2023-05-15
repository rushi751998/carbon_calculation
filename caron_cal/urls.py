"""caron_cal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = 'index'),
    path('cc', views.cc,name = 'cc'),
    path('cc_home', views.cc_home,name = 'cc_home'),    
    path('result', views.cc_result,name = 'result'),    
    path('cc_car', views.cc_car,name = 'cc_car'),
    path('cc_industry', views.cc_industry,name = 'cc_industry'),     
    path('cc_industry_result', views.cc_result_industry,name = 'cc_industry_result'),     
    path('cc_output', views.cc_output,name = 'cc_output'),
    path('trend', views.trend,name = 'trend'),
    path('forcasted_trend', views.forcasted_trend,name = 'forcasted_trend')
]
