from django.db import models
# Bring in datetime package from Python
from datetime import datetime
# Need to access other app
from agents.models import Agent
# Added Decimal Entry for Fee Payment
from decimal import Decimal


# Create your models here.

# Extending the core model
# The DO-NOTING leaves the listing of artist alone even if it gets deleted!


class Artist(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    party = models.IntegerField()
    contact = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    accomodation = models.BooleanField(default=True)
    flights = models.BooleanField(blank=True)
    transport = models.BooleanField(default=True)
    rider = models.BooleanField(default=True)
    venue = models.BooleanField(default=True)
    site = models.URLField(blank=True, null=True)
    # Photo folder being directed to main admin folder in static
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    # Date and Time
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    # Title to be the main field to display
    def __str__(self):
        return self.title
