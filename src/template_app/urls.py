from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_page, name='index'),
    path('list', views.list_page, name='list'),
    path('admin/', admin.site.urls),
]
