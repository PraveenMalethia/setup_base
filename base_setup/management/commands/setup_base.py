from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
from pathlib import Path

UTILS_DIR = BASE_DIR = Path(__file__).resolve().parent / 'utils'
TEMPLATES_DIR = BASE_DIR = Path(__file__).resolve().parent / 'utils/templates'

class Command(BaseCommand):
    help = 'Displays current time'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='App Name')

    def handle(self, *args, **kwargs):
        app_name = kwargs.get('app_name',None)
        # path of new app
        if app_name is not None:
            newapp_path = settings.BASE_DIR / kwargs.get('app_name')
            if not os.path.exists(newapp_path):
                # create app directory
                os.makedirs(newapp_path)
                # create init.py
                init_py = open(str(newapp_path)+"\__init__.py", "w")
                # create admin.py
                admin = open(str(newapp_path)+"\\admin.py", "w")
                admin_dummy = open(str(UTILS_DIR/"admin.py"), "r")
                admin.write(admin_dummy.read())
                # create apps.py
                apps = open(str(newapp_path)+"\\apps.py", "w")
                apps_dummy = open(str(UTILS_DIR/"apps.py"), "r")
                data = apps_dummy.read()
                data = data.replace("AppCapitalName", kwargs.get('app_name').capitalize())
                data = data.replace("AppName", kwargs.get('app_name'))
                # write apps.py
                apps.write(data)
                # create models.py
                models = open(str(newapp_path)+"\models.py", "w")
                models_dummy = open(str(UTILS_DIR/"models.py"), "r")
                # write models.py
                models.write(models_dummy.read())
                # create test.py
                tests = open(str(newapp_path)+"\\tests.py", "w")
                test_dummy = open(str(UTILS_DIR/"tests.py"), "r")
                # write test.py
                tests.write(test_dummy.read())
                # create urls.py
                urls = open(str(newapp_path)+"\\urls.py", "w")
                urls_dummy = open(str(UTILS_DIR/"urls.py"), "r")
                # write urls.py
                urls.write(urls_dummy.read())           
                # create views.py
                views = open(str(newapp_path)+"\\views.py", "w")
                views_dummy = open(str(UTILS_DIR/"views.py"), "r")
                # write views.py
                views.write(views_dummy.read())
                os.makedirs(newapp_path / 'migrations')
                os.makedirs(newapp_path / 'templates')
                os.makedirs(newapp_path / 'static')
                os.makedirs(newapp_path / 'static/js')
                os.makedirs(newapp_path / 'static/css')
                os.makedirs(newapp_path / 'static/img')
                migrations = open(str(newapp_path / 'migrations')+"\__init__.py", "w")
                index_html = open(str(newapp_path / 'templates')+"\index.html", "w")
                js_file = open(str(newapp_path / 'static/js')+"\index.js", "w")
                style_file = open(str(newapp_path / 'static/css')+"\style.css", "w")
                index_html_dummy = open(str(TEMPLATES_DIR/"index.html"), "r")
                index_html.write(index_html_dummy.read())            
                self.stdout.write(self.style.SUCCESS('Your App has been successfully created.'))
            else:
                raise CommandError('App already exists. please try with a different name.')
        else:
            self.stdout.write(self.style.ERROR('Please add a name for your app after setup_base <<app_name>>.'))