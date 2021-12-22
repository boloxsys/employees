from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbempleado',
        'USER': 'jbolo',
        'PASSWORD': '****',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_URL = '/static/'

