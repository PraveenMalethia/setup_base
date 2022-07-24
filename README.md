=====
Django Base Setup
=====

"Django Base Setup" is a Django app to help you setup a basic Django project.


Quick start
-----------

1. Add "basesetup" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'basesetup',
    ]

2. Include the basesetup URLconf in your project urls.py like this::

    path('', include('basesetup.urls')),

3. Run ``python manage.py setup_base <<app_name>>`` to create the basic app.

4. Start the development server and visit http://127.0.0.1:8000/ (you'll see Obiwan-Kenobi).
