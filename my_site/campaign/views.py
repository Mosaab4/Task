from django.shortcuts import render
from django.views.generic import ListView

from .models import Campaign

# Create your views here.

class CampaignListView(ListView):
    model = Campaign
    context_object_name = 'campaigns'
    template_name = 'campaign/list.html'
