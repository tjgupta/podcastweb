from .settings import *

DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

PODCAST_APP.update({'base_url': 'http://127.0.0.1:8000'})

# config/local.py is git ignored to allow for easy settings
# overrides without affecting others environments / developers
try:
    from .local import *
except ImportError:
    pass
