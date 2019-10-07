""" Production settings for heroku hosting """

from mysite.base import (DATABASES, INSTALLED_APPS, MIDDLEWARE)
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Add compression and caching support for Whitenoise
# http://whitenoise.evans.io/en/stable/django.html#add-compression-and-caching-support
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Using Whitenoise in development env
# http://whitenoise.evans.io/en/stable/django.html#using-whitenoise-in-development
if DEBUG == True:
    INSTALLED_APPS += [
        'whitenoise.runserver_nostatic',
    ]

# Enable WhiteNoise
# http://whitenoise.evans.io/en/stable/django.html#enable-whitenoise
MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# WSGI application for heroku hosting
WSGI_APPLICATION = 'mysite.heroku.wsgi.application'

# dj-database-url package
# https://pypi.org/project/dj-database-url/
db_from_env = dj_database_url.config(conn_max_age=500)

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES['default'].update(db_from_env)
