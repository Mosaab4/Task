from django import forms
from django.forms import SelectDateWidget

from .models import Campaign

class CampaignForm(forms.ModelForm):


    stop_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date', 
                'class': 'form-control'
                }
        )
    )
    class Meta:
        model = Campaign
        fields = (
            'name',
            'status',
            'type',
            'stop_date',
            'description',
        )