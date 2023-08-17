
from django.contrib import admin
from django.urls import path, include
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register', views.register),
]
