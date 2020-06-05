from django.shortcuts import render

# Create your views here.
# Render a request to view to the page
# THESE PATHS GO BY THE "TEMPLATES" FOLDER IN THE ROOT!
def index(request):
  return render(request, 'artists/artists.html')

  
def artist(request):
  return render(request, 'artists/artist.html')


def search(request):
  return render(request, 'artists/search.html')