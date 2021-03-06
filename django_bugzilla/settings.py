from pathlib import Path
import os
import dj_database_url

from os.path import join, dirname
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

dotenv_path = join(BASE_DIR, '.env')
load_dotenv()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'DEBUG'

ALLOWED_HOSTS = ['127.0.0.1','djangobugzilla.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # project apps
    # 'corsheaders',
    'core',
    'users',
    'ticket',
    'project',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'django_bugzilla.urls'

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
            # register custom template_tags here
            'libraries':{
            'custom_notification_tag': 'core.templatetag.custom_notification_tag'
            }
        },
    },
]

WSGI_APPLICATION = 'django_bugzilla.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# LOCAL DEVELOPMENT DATABASE SETTINGS
# DATABASES = {
#     'default': {
#         'ENGINE'   : os.getenv("DATABASE_ENGINE"),
#         'NAME'     : os.getenv("DATABASE_NAME"),
#         'USER'     : os.getenv("DATABASE_USER"),
#         'PASSWORD' : os.getenv("DATABASE_PASSWORD"),
#         'HOST'     : os.getenv("DATABASE_HOST"),
#         'PORT'     : os.getenv("DATABASE_PORT") ,
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE'   : "DATABASE_ENGINE",
#         'NAME'     : "DATABASE_NAME",
#         'USER'     : "DATABASE_USER",
#         'PASSWORD' : "DATABASE_PASSWORD",
#         'HOST'     : "DATABASE_HOST",
#         'PORT'     : "DATABASE_PORT" ,
#         'OPTIONS'  : {
#                     "sslmode": "SSL_MODE",
#                     "sslrootcert": os.path.join(BASE_DIR, "SSL_ROOT_CERT")
#                     }
#     }
# }
import dj_database_url


db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/images/'

MEDIA_ROOT = BASE_DIR / 'static/images'



AUTH_USER_MODEL = 'core.BugUser'

LOGIN_URL = "/signup"

## LOCAL DEVELOPMENT SETTINGS
# from pathlib import Path
# import os
# # import dj_database_url

# from os.path import join, dirname
# from dotenv import load_dotenv

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

# dotenv_path = join(BASE_DIR, '.env')
# load_dotenv()

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.getenv("SECRET_KEY")

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG")

# ALLOWED_HOSTS = ['127.0.0.1','djangobugzilla.herokuapp.com']


# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'whitenoise.runserver_nostatic',
#     'django.contrib.staticfiles',
#     # project apps
#     # 'corsheaders',
#     'core',
#     'users',
#     'ticket',
#     'project',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'whitenoise.middleware.WhiteNoiseMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     # 'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# # CORS_ORIGIN_ALLOW_ALL = True

# ROOT_URLCONF = 'django_bugzilla.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#             # register custom template_tags here
#             'libraries':{
#             'custom_notification_tag': 'core.templatetag.custom_notification_tag'
#             }
#         },
#     },
# ]

# WSGI_APPLICATION = 'django_bugzilla.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': BASE_DIR / 'db.sqlite3',
# #     }
# # }

# DATABASES = {
#     'default': {
#         'ENGINE'   : os.getenv("DATABASE_ENGINE"),
#         'NAME'     : os.getenv("DATABASE_NAME"),
#         'USER'     : os.getenv("DATABASE_USER"),
#         'PASSWORD' : os.getenv("DATABASE_PASSWORD"),
#         'HOST'     : os.getenv("DATABASE_HOST"),
#         'PORT'     : os.getenv("DATABASE_PORT") ,
#     }
# }


# # db_from_env = dj_database_url.config(conn_max_age=600)
# # DATABASES['default'].update(db_from_env)

# # Password validation
# # https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/3.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_L10N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.1/howto/static-files/

# STATIC_URL = '/static/'

# # STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [ BASE_DIR / 'static']
# # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_URL = '/images/'

# MEDIA_ROOT = BASE_DIR / 'static/images'



# AUTH_USER_MODEL = 'core.BugUser'

# LOGIN_URL = "/signup"



