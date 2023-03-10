from django import forms
from .models import Calculator_form

# creating a form
class Calculator_form(forms.Form):
	Electricity_monthly = forms.IntegerField(required=False)
	Yearly_distance_travelled_petrol = forms.IntegerField(required=False)
	Yearly_distance_travelled_diesel = forms.IntegerField(required=False)
	LPG_qty = forms.IntegerField(required=False)




# class Calculator_form(forms.Form):
    # Electricity_monthly = forms.IntegerField()

    
    # class Meta:
    #     model=Calculator_form
    #     fields ="__all__"t44hrt