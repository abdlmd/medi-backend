from django.contrib import admin
from .models import ConsultRequest

class ConsultRequestAdmin(admin.ModelAdmin):
    list_display=["symptoms","description","status","created_at","patient","doctor"]
admin.site.register(ConsultRequest,ConsultRequestAdmin)

# Register your models here.
