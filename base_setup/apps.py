from django.apps import AppConfig


class BasesetupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_setup'
