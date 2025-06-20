from . import views
from django.urls import path

urlpatterns=[
    path('create_consult_request/',views.create_consult_request,name="create_consult_request"),
    path('get_all_consult_requests/',views.get_all_consult_requests,name="get_all_consult_requests"),
    path('get_my_consult_requests/',views.get_my_consult_requests,name="get_my_consult_requests"),
    path("get_pending_requests/",views.get_pending_requests,name="get_pending_requests"),
    path('confirm_consult_request/<int:pk>/',views.confirm_consult_request,name="confirm_consult_request"),
    path('get_my_volunteered_consult_requests/',views.get_my_volunteered_consult_requests,name="get_my_volunteered_consult_requests")
]