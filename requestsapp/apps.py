from django.apps import AppConfig

# App configuration for the requestsapp application
# Django uses this class to identify and initialize the app
class RequestsappConfig(AppConfig):
    # Default type for automatically created primary keys in models
    default_auto_field = 'django.db.models.BigAutoField'
    #name of the app
    name = 'requestsapp'
