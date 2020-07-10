from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from contacts.models import Contact

# Create your views here.


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, 'Username is Taken! Please use another username.')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, 'Email is Taken! Please use another email.')
                    return redirect('register')
                else:
                    # All good!
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Register THEN Login
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'Successfully Registered.')
                    return redirect('login')

        # Indentation in Python a bit tricky be careful!
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authethicate method inbuilt from Django
        user = auth.authenticate(username=username, password=password)

        # Login in using login method
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Welcome Back!')
            return redirect('search')


        else:
            messages.error(request, 'Invalid Credentials.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.error(request, 'Logged Out User')
        return redirect('register')
      


def dashboard(request):
    # User to contact model to order by the user id (most recent first by user)
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    # Pass through context below
    context = {
        'contacts' : user_contacts
    }
    return render(request, 'accounts/dashboard.html', context)
