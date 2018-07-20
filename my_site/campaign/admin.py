from django.contrib import admin
from .models import Type, Campaign

# Register your models here.

class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'status',
        'type',
        'stop_date',
    )

    list_filter = ('status','type')
    search_fields = ('name','description')

admin.site.register(Type)
admin.site.register(Campaign,CampaignAdmin)