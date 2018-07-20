from django.urls import path, include
from .views import CampaignListView

app_name = 'campaign'

urlpatterns = [
    path('', CampaignListView.as_view(), name='list'),
]