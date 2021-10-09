from .settings import *

DEBUG = True

SECRET_KEY = '8_cif8xx6w#7s+%+y(q0e6x3#p-oa2ud4po^y_lj(mo+0j-vt&'

DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3',)
    }
}


ALLOWED_HOSTS = ['127.0.0.1']
