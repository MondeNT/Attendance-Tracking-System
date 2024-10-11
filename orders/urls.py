from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name ='index'),
    path('clock/', views.employee, name ='clock'),
    path('forgotPwd/', views.forgotPwd, name ='forgotPwd'),
    path('adminPage/', views.adminPage, name ='adminPage'),
]
