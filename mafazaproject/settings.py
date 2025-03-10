"""
Django settings for mafazaproject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
CSRF_TRUSTED_ORIGINS = [
    "https://mafaza-production.up.railway.app",
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-a#_j#6h2l-a^57s((zi_*g-m!y8ywv5a7jn=9i94p+t&#m1&)y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "mafaza-production.up.railway.app",
    "127.0.0.1",
    "localhost",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mafazapp',
    'django_countries',

]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mafazaproject.urls'

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

WSGI_APPLICATION = 'mafazaproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',  # or another engine (e.g., PostgreSQL)
#         'NAME': BASE_DIR / "db.sqlite3",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # or another engine (e.g., PostgreSQL)
        'NAME': 'railway',
        'USER' : 'postgres',
        'PASSWORD': 'OGsfquDDgpcRXgdfTGWOREkHQREsCJfj',
        'HOST': 'caboose.proxy.rlwy.net',
        'PORT': '21376',
    }
}

DATABASE_URL = os.getenv('postgresql://postgres:OGsfquDDgpcRXgdfTGWOREkHQREsCJfj@caboose.proxy.rlwy.net:21376/railway')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'mafazapp.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = '/static/'

# For collecting static files during deployment
STATIC_ROOT = BASE_DIR / "staticfiles"

# Ensure the path is correct for development static files
STATICFILES_DIRS = [
    BASE_DIR / "mafazapp" / "static",
]

# Optional: Middleware to serve static files in development
if not DEBUG:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"





MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Ensure cache is disabled for authenticated pages
CACHE_MIDDLEWARE_SECONDS = 0  # Disable caching entirely
CACHE_MIDDLEWARE_KEY_PREFIX = ''  # Optional


SESSION_COOKIE_AGE = 1209600  # Two weeks
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep session active when the browser is closed

# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Redis as the message broker
