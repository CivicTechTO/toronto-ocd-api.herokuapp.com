import os
import datetime
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

def envvar(name, default=None):
    result = os.environ.get(name, default)
    if result is None:
        raise ImproperlyConfigured('missing required environment variable ' + name)
    return result

# env variables
SECRET_KEY = envvar('SECRET_KEY', 'ITSASECRET')
RAVEN_DSN = envvar('RAVEN_DSN', '')
ALLOWED_HOSTS = envvar('ALLOWED_HOSTS', '*').split(',')
DATABASES = {'default': dj_database_url.config(default='postgis://eric:@localhost/opencivicdata')}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
ELASTICSEARCH_HOST = envvar('ELASTICSEARCH_HOST', 'http://localhost:9200')
TEMPLATE_DEBUG = DEBUG = envvar('DJANGO_DEBUG', 'False').lower() == 'true'
USE_LOCKSMITH = envvar('USE_LOCKSMITH', 'false').lower() == 'true'
if USE_LOCKSMITH:
    LOCKSMITH_SIGNING_KEY = envvar('LOCKSMITH_SIGNING_KEY')


# settings we don't override
#TIME_ZONE = 'America/New_York'
#USE_TZ = True
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'ocdapi.urls'

TEMPLATE_DIRS = (
    os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),
)
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'boundaries',
    'opencivicdata.apps.BaseConfig',
    'imago',
    'pupa',
    'rest_framework',
)
if RAVEN_DSN:
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
    RAVEN_CONFIG = {'dsn': RAVEN_DSN}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'default':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'boundaries': {
             'handlers': ['console'],
             'level': 'INFO',
             'formatter': 'simple'
        },
    }
}

# locksmith stuff
if USE_LOCKSMITH:
    INSTALLED_APPS += ('locksmith.auth.apps.LocksmithAuthConfig',)
    MIDDLEWARE_CLASSES += ('locksmith.auth.middleware.APIKeyMiddleware',)
    LOCKSMITH_REGISTRATION_URL = 'http://sunlightfoundation.com/api/accounts/register/#ocd'
    LOCKSMITH_HUB_URL = 'http://sunlightfoundation.com/api/analytics/'
    LOCKSMITH_API_NAME = 'opencivicdata'

BOUNDARIES_SHAPEFILES_DIR = 'shapefiles'
IMAGO_COUNTRY = 'us'
IMAGO_BOUNDARY_MAPPINGS = {
    'nyc-council-districts': {'key': 'placeholder_id',
                              'prefix': '',
                              'ignore': None,
                             },
    'new-york-municipal': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'chicago-municipal': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'chicago-wards-2015': {'key': 'placeholder_id',
                           'prefix': '',
                           'ignore': None,
                          },
    'chicago-precincts-2015': {'key': 'placeholder_id',
                               'prefix': '',
                               'ignore': None,
                              },
    'st-paul-municipal': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'st-paul-wards': {'key': 'placeholder_id',
                      'prefix': '',
                      'ignore': None,
                     },
    'st-paul-precincts': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'illinois-lower-2011': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },
    'illinois-upper-2011': {'key': 'placeholder_id',
                          'prefix': '',
                          'ignore': None,
                         },

}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny',),
    'PAGE_SIZE': 10
}
