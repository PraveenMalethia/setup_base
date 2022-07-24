from django.core.management.base import BaseCommand, CommandError
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

class Command(BaseCommand):
    help = 'Displays current time'
    def handle(self, *args, **kwargs):
        app_name = kwargs.get('app_name',None)
        # path of new app
        if app_name is not None:
            newapp_path = BASE_DIR.parent.parent / kwargs.get('app_name')
            if not os.path.exists(newapp_path):
                # create app directory
                os.makedirs(newapp_path)
                # create init.py
                init_py = open(str(newapp_path)+"\__init__.py", "w")
                # create admin.py
                admin = open(str(newapp_path)+"\\admin.py", "w")
                admin.write("""from django.contrib import admin\n\n# Register your models here.""")
                # create apps.py
                apps = open(str(newapp_path)+"\\apps.py", "w")
                # write apps.py
                apps.write(f"""
from django.apps import AppConfig

class {app_name.capitalize()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{app_name}'
""")
                # create models.py
                models = open(str(newapp_path)+"\models.py", "w")
                # write models.py
                models.write("""from django.db import models\n\n# Create your models here.""")
                # create test.py
                tests = open(str(newapp_path)+"\\tests.py", "w")
                # write test.py
                tests.write("""from django.test import TestCase\n\n# Create your tests here.""")
                # create urls.py
                urls = open(str(newapp_path)+"\\urls.py", "w")
                # write urls.py
                urls.write("""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index),
]

""")            
                # create views.py
                views = open(str(newapp_path)+"\\views.py", "w")
                # write views.py
                views.write("""
from django.shortcuts import render

# Create your views here.

def Index(request):
    return render(request, 'index.html')
""")
                os.makedirs(newapp_path / 'migrations')
                os.makedirs(newapp_path / 'templates')
                os.makedirs(newapp_path / 'static')
                os.makedirs(newapp_path / 'static/js')
                os.makedirs(newapp_path / 'static/css')
                os.makedirs(newapp_path / 'static/img')
                migrations = open(str(newapp_path / 'migrations')+"\__init__.py", "w")
                index_html = open(str(newapp_path / 'templates')+"\index.html", "w")
                index_html.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
</head>
<body>
    <div
      style="width: 100%; height: 0; padding-bottom: 43%; position: relative"
    >
      <iframe
        src="https://giphy.com/embed/xTiIzJSKB4l7xTouE8"
        width="100%"
        height="100%"
        style="position: absolute"
        frameborder="0"
        class="giphy-embed"
        allowfullscreen
      ></iframe>
    </div>
    <p>
      <a
        href="https://giphy.com/gifs/starwars-star-wars-episode-3-xTiIzJSKB4l7xTouE8"
        >via GIPHY</a
      >
    </p>
  </body>
</html>

""")            
                self.stdout.write(self.style.SUCCESS('Your App has been successfully created.'))

        else:
            self.stdout.write(self.style.ERROR('Please add a name for your app after setup_base <<app_name>>.'))