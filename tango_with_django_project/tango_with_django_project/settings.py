"""
Django settings for tango_with_django_project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print __file__
print os.path.dirname(__file__)
print os.path.dirname(os.path.dirname(__file__))

#Code to add a path to templates I created

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows
    # Don't forget to use absolute paths, not relative paths.
    # 'code/tango_with_django_project/', This is replaced with TEMPLATE_PATH
    TEMPLATE_PATH,
)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm@!&y(*qcet)ne=69tf%d-ns*h5ay)$^6_e!t51n8y2c^0(2eu'

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
    'rango',
##    'registration',
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

ROOT_URLCONF = 'tango_with_django_project.urls'

WSGI_APPLICATION = 'tango_with_django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_PATH = os.path.join(BASE_DIR, 'static')

#STATIC_URL defines the base URL with which Django apps will find static
# media files when the server is running
STATIC_URL = '/static/'

#Allows you to specify the location of the static directory on the local disk
STATICFILES_DIRS = (
    STATIC_PATH,
)

#Defines the base URL from which all media files will be accessible on the
#development server
MEDIA_URL = '/media/'

#Used to tell Django where uploaded files should be stored on the local disk
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #Absolute path to the media directory

#This ensures that the login_required() decorator will redirect any user not
#authorized
LOGIN_URL = '/rango/login/'

#Setting up a Registration Package
##REGISTRATION_OPEN = True #If true, users can register
##ACCOUNT_ACTIVATION_DAYS = 7 #One-week activation window. Can be changed
##REGISTRATION_AUTO_LOGIN = True #If true, the user will be auto logged in
##LOGIN_REDIRECT_URL = '/rango/' #Will redirect after successful login
##LOGIN_URL = '/accounts/login/' #Will redirect after failed login
