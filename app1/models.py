from django.db import models

# class calculations(models.Model):
#     caption=models.DateField(default="NA")
#     video=models.FileField(upload_to="video")
#     processed_video=models.FileField(upload_to="processed_video",default="Na")
    
class Calculator_form(models.Model):
	Electricity_monthly = models.IntegerField()
	Yearly_distance_travelled_petrol = models.IntegerField()
	Yearly_distance_travelled_diesel = models.IntegerField()
	LPG_qty = models.IntegerField()
