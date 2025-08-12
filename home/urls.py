from django.contrib import admin
from django.urls import path

from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('upload/', views.main, name='upload_excel'),
    path('data/', views.view_data, name='view_data'), 
    path('scannersheet', views.ScannerSheet, name='Scanner_Sheet'), 
    path('dataEnter', views.dataEntry, name='data_Entry'), 
    path('setLocation', views.setlocation, name='set_location'), 
    path('media', views.upload_form, name='Media'), 
    path('master', views.upload_master, name='Master'), 
    path('home', views.home, name='Home'), 
    path('scanner', views.scannerFile, name='Scanner'), 




]