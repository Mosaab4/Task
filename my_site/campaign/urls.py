from django.urls import path, include
from .views import CampaignListView, AddView

app_name = 'campaign'

urlpatterns = [
    path('', CampaignListView.as_view(), name='list'),
    path('add/', AddView.as_view(), name='add'),
]