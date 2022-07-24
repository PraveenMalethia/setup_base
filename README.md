=====
Django Base Setup
=====

"Django Base Setup" is a Django app to help you setup a basic Django project.


Quick start
-----------

1. Add "base_setup" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'base_setup',
    ]

2. Run ``python manage.py setup_base <<app_name>>`` to create the basic app.

3. Start the development server and visit http://127.0.0.1:8000/ (you'll see Obiwan-Kenobi).
