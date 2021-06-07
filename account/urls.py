from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('register/',views.userregister,name='register'),
    path('login/',views.userlogin,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('account/',views.account_view,name='account'),
    path('changepassword/',views.changepassword,name='changepassword'),

]

