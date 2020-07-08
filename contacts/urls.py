from django.urls import path

from . import views

# Contacts Url for {{ url 'contact' }}
urlpatterns = [
    path('contact', views.contact, name='contact')
]