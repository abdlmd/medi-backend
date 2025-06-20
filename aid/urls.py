from . import views
from django.urls import path
urlpatterns=[
    path('create_aid_request/',views.create_aid_request,name="create_aid_request"),
    path('get_aid_requests/',views.get_aid_requests,name="get_aid_requests"),
    path('volunteer_for_request/<int:pk>/',views.volunteer_for_request,name="volunteer_for_request"),
    path('get_my_posted_request/',views.get_my_posted_request,name="get_my_posted_request"),
    path('get_my_volunteered_request/',views.get_my_volunteered_request,name="get_my_volunteered_request"),
    path('get_aid_by_type/<str:type_name>/',views.get_aid_by_type,name="get_aid_by_type")
]