from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
# Create your views here.

def contact(request):
    # Make sure it is a post request
    if request.method == 'POST':
        artist_id = request.POST['artist_id']
        title = request.POST['title']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']

        # Check if user has made inquiry already and output message
        # If the user is logged in but you made a enquiry on this artist already
        # Logged in users don't make double enquirys
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(artist_id=artist_id, user_id=user_id)
            # If contacted throw the error of you already made a enquiry
            if has_contacted:
                messages.error(request, 'You have already made a enquiry for this artist!')
                return redirect('/artists/'+artist_id)


        # Define variables to POST
        contact = Contact(title=title, artist_id=artist_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        # Save
        contact.save()

        #  CANT HAVE THIS FEATURE ON LIVE SERVER OF AREAAGENCY.LIVE (SENDS ME BACK A 500 RESPONSE!)
        # # Send Email to Gmail Config
        # send_mail(
        #     'Artist Roster Enquiry | Area Agency',
        #     'There has been enquiry for ' + title + '. Sign into the Dashboard panel of Area Agency for more info!',
        #     'matthewlukebyrne@gmail.com',
        #     [agent_email, 'matthewlukebyrne@gmail.com'],
        #     fail_silently=False
        # )

        # Message Success with a redirect back to artists page!
        messages.success(request, 'Your request has been notifed! Our Area Agents will get back to you soon...')
        return redirect('/artists/'+artist_id)

        
