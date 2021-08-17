from django.contrib import admin
from django.urls import path
import lists

urlpatterns = [
    path('', lists.views.home_page, name='home'),
    path('admin/', admin.site.urls),
]
