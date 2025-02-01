"""
Django settings for prodTasksProj project.

Generated by 'django-admin startproject' using Django 5.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
from environ import Env
env = Env()
Env.read_env()
ENVIRONMENT=env('ENVIRONMENT', default='production')



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')
SECRET_KEY=env('SECRET_KEY')
ENCRYPT_KEY=env('ENCRYPT_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
#DEBUG = bool(int(os.environ.get('DEBUG', 0)))
if ENVIRONMENT == 'development':
   DEBUG = True
   ALLOWED_HOSTS = ['*']
   #ALLOWED_HOSTS = [env('DEV_ALLOWED_HOSTS')]
   DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqllite3'), } }
elif ENVIRONMENT == 'production':
   DEBUG = False
   ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
   #ALLOWED_HOSTS = env('PROD_ALLOWED_HOSTS')
   #ALLOWED_HOSTS.extend(ALLOWED_HOSTS.split(','))
   DATABASES = {
      'default': {
        'ENGINE': env('ENGINE'),
        'NAME': env('NAME'),
        'USER': env('USER'),
        'PASSWORD': env('PASSWORD'),
        'HOST': env('HOST'),
        'PORT': env('PORT'),
        'OPTIONS': {'driver':'ODBC Driver 18 for SQL Server', 'extra_params':'Encrypt=no'
        },
     },
    }
print("DATABASES:")
print(DATABASES)

#ALLOWED_HOSTS = []
#ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')
#if ALLOWED_HOSTS_ENV:
#   ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))


# Application definition

INSTALLED_APPS = [
    'prodTaskApp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'prodTasksProj.urls'

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

WSGI_APPLICATION = 'prodTasksProj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = { 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqllite3'), } }

#DATABASES = {
#    'default': {
#        'ENGINE': 'mssql',
#        'NAME': 'tasks',
#        'USER': 'SA',
#        'PASSWORD': 'mySQLabcd0',
#        'HOST': '192.168.0.55',
#        'PORT': '1433',
#        'OPTIONS': {
#            'driver': 'ODBC Driver 18 for SQL Server',
#            'extra_params': "Encrypt=no" #TrustServerCertificate=no
#        },
#    },
#}



# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

#STATIC_URL = 'static/'
STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

STATIC_ROOT = '/vol/web/static'
MEDIA_ROOT = '/vol/web/media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
