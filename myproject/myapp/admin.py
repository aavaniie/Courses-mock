from django.contrib import admin
from .models import *

class Courseadmin(admin.ModelAdmin):
    list_display = ('name','tutor',)
    readonly_fields = ('credits',)
    search_fields = ('name',)
    list_filter = ('times',)
    list_per_page = 2
    
    # fieldsets = [
    #     (None, {"fields": ['name','tutor']}),
    # ]

# Register your models here.
admin.site.register(Course,Courseadmin)
admin.site.register(Times)