from django.apps import AppConfig
import os

default_app_config = 'surfacemanager.surfacemanagerConfig'

class surfacemanagerConfig(AppConfig):
    name = os.path.split(os.path.dirname(__file__))[-1]
    verbose_name = "知行"
