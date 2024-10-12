from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='index'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('clock/', views.employee, name ='clock'),
    path('forgotPwd/', views.forgotPwd, name ='forgotPwd'),
    path('adminPage/', views.adminPage, name ='adminPage'),
    path('add_employee/', views.add_employee_view, name='add_employee'),
]
