from django.contrib import admin
from .models import Dryfruit

class DryfruitAdmin(admin.ModelAdmin):
    list_display=['name']
    search_fields=['name','desc']
    list_filter=['cr_date']
admin.site.register(Dryfruit,DryfruitAdmin)