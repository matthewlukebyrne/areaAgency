from django.shortcuts import get_object_or_404, render
from .models import Artist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .choices import artists_choices, agent_choices, price_choices

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

# You need to pass in this parameter included in artists.html below


def artist(request, artist_id):

    # If i go to artist/10 which doesnt exist nothing happens so set a 404 page (import)
    # Passing in the model and the artist id
    artist = get_object_or_404(Artist, pk=artist_id)

    # Again Passing through with context
    context = {
        'artist': artist
    }
    # Pass in the context
    return render(request, 'artists/artist.html', context)


# Bring in choices.py into search render
def search(request):
  
    # This query will get all listings and order by passed into dictionary
    queryset_list = Artist.objects.order_by('-list_date')

    # Keywords with i contains a certain word to return a search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                title__icontains=keywords)

    # Search By City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # Search By Fee
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # Search By Title (Artist)
    if 'title' in request.GET:
        title = request.GET['title']
        if title:
            queryset_list = queryset_list.filter(title__iexact=title)

    context = {
        'artists_choices': artists_choices,
        'agent_choices': agent_choices,
        'price_choices': price_choices,
        'artists': queryset_list,
        'values': request.GET
    }

    return render(request, 'artists/search.html', context)

