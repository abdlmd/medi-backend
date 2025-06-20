from django.contrib import admin
from .models import Medicine
# Register your models here.
class medicine_admin(admin.ModelAdmin):
    list_display=["name","manufacturer","category","price","quantity","pharmacy","created_at","updated_at"]
    search_fields=["name","manufacturer","pharmacy"]
    list_filter=["category"]

admin.site.register(Medicine,medicine_admin)