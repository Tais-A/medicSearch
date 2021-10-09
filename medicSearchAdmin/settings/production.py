from .settings import *

DEBUG = False

SECRET_KEY = 'q@r1@4qx9!yuq@pu^_a6_db3ip5ov$aov6*zr!7&y-z7mfdmg@'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['127.0.0.1']