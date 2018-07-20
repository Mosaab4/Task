from django.urls import path, include
from .views import (
    CampaignListView, 
    AddView,
    UpdateView,
    DeleteView,
)

app_name = 'campaign'

urlpatterns = [
    path('', CampaignListView.as_view(), name='list'),
    path('add/', AddView.as_view(), name='add'),
    path('update/<int:pk>/',UpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',DeleteView.as_view(),name='delete'),
]