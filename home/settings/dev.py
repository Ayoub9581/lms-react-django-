'''Use this for development'''

from .base import *

ALLOWED_HOSTS += ['127.0.0.1', "django-react-lms.herokuapp.com"]
DEBUG = True

WSGI_APPLICATION = 'home.wsgi1.dev.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = (
    'localhost:3000',
)