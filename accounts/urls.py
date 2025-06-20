from . import views
from django.urls import path

urlpatterns=[
    path('register_user/',views.register_user,name="register_user"),
    path('update_user_profile/',views.update_user_profile,name="update_user_profile"),
    path('view_profile/',views.view_profile,name="view_profile")
]