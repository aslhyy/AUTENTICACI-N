"""
Django settings for autenticacion project.
"""

from pathlib import Path
from datetime import timedelta
import dj_database_url
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# CAMBIAR EN PRODUCCIÓN (lo manejarás desde Render con variables de entorno)
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-abc123")

# Render pone DEBUG=False automáticamente si quieres
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = ['*']


# -------------------------------------------------------------
# APPS
# -------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Dependencias
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',

    # Apps propias
    'tasks',
    'users',
]


# -------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # Render requiere esto para archivos estáticos
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CORS_ALLOW_ALL_ORIGINS = True


# -------------------------------------------------------------
# URLS & TEMPLATES
# -------------------------------------------------------------
ROOT_URLCONF = 'autenticacion.urls'

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

WSGI_APPLICATION = 'autenticacion.wsgi.application'


# -------------------------------------------------------------
# BASE DE DATOS — SQLite local / PostgreSQL en Render
# -------------------------------------------------------------
if os.getenv("RENDER"):
    # Render asigna DATABASE_URL automáticamente
    DATABASES = {
        "default": dj_database_url.config(conn_max_age=600)
    }
else:
    # Modo local (más sencillo)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# -------------------------------------------------------------
# REST FRAMEWORK + JWT
# -------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}


# -------------------------------------------------------------
# STATIC FILES (OBLIGATORIO PARA RENDER)
# -------------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
