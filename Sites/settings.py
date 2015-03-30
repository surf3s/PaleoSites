"""
Django settings for Sites project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
#import secrets

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

import Sites.secrets

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Sites.secrets.SECRET_KEY_sites

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'PaleoSites',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Sites.urls'

WSGI_APPLICATION = 'Sites.wsgi.application'

GEOS_LIBRARY_PATH = 'C:/OSGeo4W/bin/geos_c.dll'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#         'ENGINE': 'django.db.backends.sqlite3',

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'PaleoSites',
        'USER': Sites.secrets.User_sites,
        'PASSWORD': Sites.secrets.Password_sites,
        'PORT': '5433',   # default Postgres por
    }
}

POSTGIS_VERSION = (2, 1, 5)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'Collected_static'),)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'Templates'),
)

FIXTURE_DIRS = (
    os.path.join(BASE_DIR,  'Fixtures'),
)