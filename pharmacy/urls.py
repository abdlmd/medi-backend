from . import views
from django.urls import path
urlpatterns=[
    path('add_medicine/',views.add_medicine,name="add_medicine"),
    path('get_all_medicines/',views.get_all_medicines,name="get_all_medicines"),
    path('get_my_medicines/',views.get_my_medicines,name="get_my_medicines"),
    path('update_medicine/<int:pk>/',views.update_medicine,name="update_medicine"),
    path('filter_medicine/<str:category_request>/',views.filter_medicine,name="filter_medicine"),
    path('delete_medicine/<int:pk>/',views.delete_medicine,name="delete_medicine")
]