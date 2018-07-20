from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.shortcuts import redirect

from .models import Campaign
from .forms import CampaignForm
# Create your views here.

class CampaignListView(ListView):
    model = Campaign
    context_object_name = 'campaigns'
    template_name = 'campaign/list.html'


class AddView(FormView):
    template_name = 'campaign/add.html'
    form_class = CampaignForm
    model = Campaign

    def form_valid(self,form):
        self.campaing = form.save(commit=False)
        self.campaing.save()

        return redirect('campaign:list')