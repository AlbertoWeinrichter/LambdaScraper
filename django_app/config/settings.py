import os
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'asecretkey'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'quotes',
    'django_celery_beat',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "postgres",
        'USER': "postgres",
        'PASSWORD': "postgres",
        'HOST': "postgres",
        'PORT': 5432
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

#    _____  __      __  _________ .____       _____      _____ __________________      _____
#   /  _  \/  \    /  \/   _____/ |    |     /  _  \    /     \\______   \______ \    /  _  \
#  /  /_\  \   \/\/   /\_____  \  |    |    /  /_\  \  /  \ /  \|    |  _/|    |  \  /  /_\  \
# /    |    \        / /        \ |    |___/    |    \/    Y    \    |   \|    `   \/    |    \
# \____|__  /\__/\  / /_______  / |_______ \____|__  /\____|__  /______  /_______  /\____|__  /
#         \/      \/          \/          \/       \/         \/       \/        \/         \/
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')
DISCOVERY_FUNCTION = os.environ.get('DISCOVERY_FUNCTION')
DETAIL_FUNCTION = os.environ.get('DETAIL_FUNCTION')


#  _____ _____ __    _____ _____ __ __
# |     |   __|  |  |   __| __  |  |  |
# |   --|   __|  |__|   __|    -|_   _|
# |_____|_____|_____|_____|__|__| |_|

BROKER_URL = 'amqp://{user}:{password}@{hostname}/{vhost}/'.format(
    user=os.environ.get('RABBIT_ENV_USER', 'admin'),
    password=os.environ.get('RABBIT_ENV_RABBITMQ_PASS', 'mypass'),
    hostname="rabbit",
    vhost=os.environ.get('RABBIT_ENV_VHOST', ''))

BROKER_POOL_LIMIT = 1
BROKER_CONNECTION_TIMEOUT = 10

CELERY_DEFAULT_QUEUE = 'quote_harvester'
CELERY_ALWAYS_EAGER = False
CELERY_ACKS_LATE = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_DISABLE_RATE_LIMITS = False
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ['application/json']
CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_PREFETCH_MULTIPLIER = 1
CELERYD_MAX_TASKS_PER_CHILD = 1000

CELERY_IMPORTS = ('quotes.tasks',)

CELERYBEAT_SCHEDULE = {
    'quote_harvesting': {
        'task': 'topic_discovery',
        "schedule": timedelta(seconds=300),
        'args': ("Friendship",)  # a test topic to discover
    },
}
