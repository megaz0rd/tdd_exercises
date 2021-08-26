from django.contrib import admin
from django.urls import path

from lists import views

urlpatterns = [
    path('<int:list_id>/', views.view_list, name='view_list'),
    path('<int:list_id>/add_item', views.view_add_item, name='add_item'),
    path('new', views.view_new_list, name='new_lits'),
]
