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
    path('cc_industry', views.cc_result_industry,name = 'cc_industry_result'),     
    path('cc_output', views.cc_output,name = 'cc_output'),
    path('trend', views.trend,name = 'trend'),
    path('forcasted_trend', views.forcasted_trend,name = 'forcasted_trend')
]
