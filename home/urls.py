from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.loginuser, name="login"),
    path('logout', views.logoutuser, name="logout"),
    path('upload/', login_required(views.main, login_url='/login')),
    path('data/', views.view_data, name='view_data'), 
    path('scannersheet', views.ScannerSheet, name='Scanner_Sheet'), 
    path('dataEnter', views.dataEntry, name='data_Entry'), 
    path('view', views.view, name='set_location'), 
    path('media', views.upload_form, name='Media'), 
    path('master',login_required( views.upload_master,login_url='/login')), 
    path('home', views.home, name='Home'), 
    path('scanner', views.scannerFile, name='Scanner'), 
    path('user', views.userView, name='UserView'), 
    path('ss', login_required(views.differencSS, login_url='/login')),
    path('short', login_required(views.short, login_url='/login')), 
    path('excess', login_required(views.excess, login_url='/login')), 
    path('scand', login_required(views.downloadScan, login_url='/login')), 
    path('scan/', views.upload_scanning, name="ScanningFile"),

]