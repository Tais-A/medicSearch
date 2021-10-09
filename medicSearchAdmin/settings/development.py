from .settings import *

DEBUG = True

SECRET_KEY = '9d=3@^40914ol%(xot&nh9r4w+vdf(29ye65y+t&s1v#4a_h6d'

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['127.0.0.1']