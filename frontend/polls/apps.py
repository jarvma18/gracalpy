'''App config'''
from django.apps import AppConfig

class PollsConfig(AppConfig):
    '''Module config class'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
