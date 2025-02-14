from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #esse nome do app , você passa para o settings.py em INSTALLED_APPS
    ############# SEMPRE FAÇA ISSO #############
    name = 'contact'
