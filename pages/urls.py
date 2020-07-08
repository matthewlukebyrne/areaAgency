# Creating a new url for the pages app

from django.urls import path

# Importing the view of the pages file
from . import views


# PATHING - Really important otherwise info will not be displayed the page
# The idea is you need to have a URL for the home page
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]
