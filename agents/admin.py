from django.contrib import admin

# Register your models here.

from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'hire_date', 'description', 'is_mvp')
    list_display_links = ('name'),
    search_fields = ('name'),
    list_per_page = 10

admin.site.register(Agent, AgentAdmin)