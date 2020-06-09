from django.shortcuts import render
from .models import Artist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# Render a request to view to the page
# THESE PATHS GO BY THE "TEMPLATES" FOLDER IN THE ROOT!
# Pass in values into a template and return render "context" as a dictionary
def index(request):
    artist = Artist.objects.order_by('-list_date').filter(is_published=True)

    # Adds a paginator functionality (6 items on artist page)
    paginator = Paginator(artist, 6)
    page = request.GET.get('page')
    paged_artists = paginator.get_page(page)

    # Context as a dictionary (then updated with paginaton to paged_artists above)
    context = {
        'artists': paged_artists
    }

    # Index
    return render(request, 'artists/artists.html', context)
  
def artist(request, artist_id):
  return render(request, 'artists/artist.html')


def search(request):
  return render(request, 'artists/search.html')