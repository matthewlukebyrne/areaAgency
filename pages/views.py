from django.shortcuts import render
from django.http import HttpResponse
# Bring in dictionary for chooices.py
from artists.choices import artists_choices, agent_choices, price_choices

# You can bring in models from anywhere so bringing in the artist model
from artists.models import Artist
from agents.models import Agent

# Create your views here.
# Renders both index and about pages below (templates folder)

# Added below is show published entries on the index only to be true at a limit of 3


def index(request):
    # Only 3 Listings!
    artists = Artist.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    # Creating a context variable like the other views and then pass that context below
    # ALSO ADDED choices.py for searching functions
    context = {
        'artists': artists,
        'artists_choices': artists_choices,
        'agent_choices': agent_choices,
        'price_choices': price_choices
    }

    # Pass into the index html
    return render(request, 'pages/index.html', context)


# Agent of the Month along with organsing by hire date below (-hire_date)
def about(request):
    agents = Agent.objects.order_by('-hire_date')

    # Get MVP
    mvp_agents = Agent.objects.all().filter(is_mvp=True)

    context = {
        'agents': agents,
        'mvp_agents': mvp_agents
    }

    return render(request, 'pages/about.html', context)
