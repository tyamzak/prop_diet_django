from django.urls import path
from django.contrib import admin
from sotuken import views
from . import views

urlpatterns = [
    path('',views.Login,name='Login'),
    path('logout',views.Logout,name='Logout'),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path('home',views.home,name='home'),
    path('keisan',views.keisan,name='keisan'),
]