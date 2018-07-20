from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import (
    ListView, 
    FormView,
    UpdateView,
    DeleteView
)



from .models import Campaign
from .forms import CampaignForm
# Create your views here.

class CampaignListView(ListView):
    model = Campaign
    context_object_name = 'campaigns'
    template_name = 'campaign/list.html'


class AddView(LoginRequiredMixin,FormView):
    template_name = 'campaign/add.html'
    form_class = CampaignForm
    model = Campaign

    def form_valid(self,form):
        self.campaign = form.save(commit=False)
        self.campaign.save()

        return redirect('campaign:list')

class UpdateView(LoginRequiredMixin,UpdateView):
    model = Campaign
    template_name = 'campaign/add.html'
    form_class = CampaignForm
    pk_url_kwarg = 'pk'

    def form_valid(self,form):
        self.campaign = form.save(commit=False)
        self.campaign.save()

        return redirect('campaign:list')

class DeleteView(LoginRequiredMixin,DeleteView):
    model = Campaign
    pk_url_kwarg = 'pk'	


    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('campaign:list')


    