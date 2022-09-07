from django.apps import AppConfig

from djangoshop.settings import LANGUAGE_CODE


class WebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web'
    if LANGUAGE_CODE == 'ru-ru':
        verbose_name = 'Сайт'
    else:
        verbose_name = 'Site'
