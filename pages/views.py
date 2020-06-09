from django.shortcuts import render
from django.http import HttpResponse

# Bring in Artist model to show on the index age
from artists.models import Artist
# Bring in Agents to show in About page
from agents.models import Agent

# Views can let you render the information to the screen
# Create your views here.
def index(request):
    # Only 3 Listings!
    artists = Artist.objects.order_by('-list_date').filter(is_published=True)[:3]

    # Creating a context variable like the other views and then pass that context below
    # ALSO ADDED choices.py for searching functions
    context = {
        'artists' : artists
    }

    # Pass into the index html
    return render(request, 'pages/index.html', context)

# Agent of the Month along with organsing by hire date below (-hire_date)
def about(request):
    agents = Agent.objects.order_by('-hire_date')

    # Get MVP
    mvp_agents = Agent.objects.all().filter(is_mvp=True)

    context = {
        'agents' : agents,
        'mvp_agents' : mvp_agents
    }

    return render(request, 'pages/about.html', context)