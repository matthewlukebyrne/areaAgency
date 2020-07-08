from django.db import models
from datetime import datetime

# Creation of the enquire in the single artist page. Enquires about booking a act

class Contact(models.Model):
    title = models.CharField(max_length=200)
    artist_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateField(default=datetime.now, blank=True)
    # Connected to whatever user is logged in on the DASHBOARD (important)
    user_id = models.IntegerField(blank=True)
    def __str__(self):
        return self.name
