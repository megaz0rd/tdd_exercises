from django.contrib import admin
from django.urls import path

from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('lists/<int:list_id>/', views.view_list, name='view_list'),
    path('lists/<int:list_id>/add_item', views.view_add_item, name='add_item'),
    path('lists/new', views.view_new_list, name='new_lits'),
]
