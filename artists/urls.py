# Creating a new url for the pages app

from django.urls import path

# Importing the view of the pages file
from . import views


# PATHING - Really important otherwise info will not be displayed the page
# The idea is you need to have a URL for the home page

# artists/artist_id pathway in the URL
urlpatterns = [
    path('', views.index, name='artists'),
    path('<int:artist_id>', views.artist, name='artist'),
    path('search', views.search, name='search')
]