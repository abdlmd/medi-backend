from django.contrib import admin
from .models import AidRequest
# Register your models here.
class aid_request_admin(admin.ModelAdmin):
    list_display=["title","description","types","created_by","created_at","updated_at","fulfilled_status","fulfilled_by"]
admin.site.register(AidRequest,aid_request_admin)
