
from django.urls import path
from . import views

app_name='bankapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('blank/', views.blank, name='blank'),
    path('newpage/',views.newpage, name='newpage'),
    path('logout/',views.logout, name='logout'),

]

