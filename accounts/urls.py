# Accessing the "auth_user" data tables already preloaded inside Django Framework (this can be viewd inside Postgres!)

# Creating a new url for the accounts app

from django.urls import path

# Importing the view of the pages file
from . import views

# PATHING - Really important otherwise info will not be rendered to the page
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]