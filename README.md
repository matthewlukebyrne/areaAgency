# areaAgency
College project version for Area Agency system.

![area-agency](1.PNG)
![area-agency](2.PNG)
![area-agency](3.PNG)

# Documentation
https://www.djangoproject.com/ <br>
https://jinja.palletsprojects.com/en/2.11.x/

# Tools and Technologies Used
Django <br>
Postgres (phpMyAdmin) <br>
Bootstrap4 <br>
JQuery <br>
SCSS Files <br>

# Installation and Used Commands
<code>python manage.py runserver</code>
-runs the server

<code>python manage.py runmigrations</code>
-transfer the model data over to postgres

<code>python manage.py startapp pages</code>
-Creates a new pages app

<code>python manage.py collectstatic</code>
-shows a static folder in the root

<code>python manage.py startapp artists</code>
-created a artists app (needs a urls.py)

<code>python manage.py startapp agents</code>
-creates a agents app (needs a urls.py)

<code>python manage.py migrate</code>
-Check postgres database to see if it's active and running

<code>python manage.py makemigrations</code>
-Attempt to enter fields into models and then pass them Postgres


# Deployment Stage 
Coming! <br>
https://www.nginx.com/ <br>
https://www.digitalocean.com/ <br>
https://gunicorn.org/ <br>
