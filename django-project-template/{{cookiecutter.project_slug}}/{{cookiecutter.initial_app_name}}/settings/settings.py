import os
import platform
from pathlib import Path

import environ
from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
env = environ.Env()
READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))

env = environ.FileAwareEnv(
    DEBUG=(bool, False),
)

# GENERAL
# ------------------------------------------------------------------------------

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-wu9#po37gfc6e$9bg#qt&fqk42+flc8zp^4xj)(=etm@_lg%#8",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["localhost", "127.0.0.1"])
CSRF_TRUSTED_ORIGINS = env.list(
        "DJANGO_CSRF_TRUSTED_ORIGINS", default=["http://localhost", "http://127.0.0.1"]
)

# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
{%- if cookiecutter.use_allauth %}
    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.orcid',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.slack',
{%- endif %}
{%- if cookiecutter.use_tailwind %}
    # tailwind
    'tailwind',
    '{{ cookiecutter.initial_app_name }}.theme',
{%- endif %}
{%- if cookiecutter.use_obj_storage %}
    # obj storage
    'storages',
{%- endif %}

    # local apps
    'test_app1',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
{% if cookiecutter.use_allauth %}
    # allauth
    'allauth.account.middleware.AccountMiddleware',
{% endif %}
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

X_FRAME_OPTIONS = "SAMEORIGIN"

ROOT_URLCONF = '{{ cookiecutter.initial_app_name }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "{{ cookiecutter.initial_app_name }}/templates"],
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

WSGI_APPLICATION = "{{ cookiecutter.initial_app_name }}.wsgi.application"
ASGI_APPLICATION = "{{ cookiecutter.initial_app_name }}.asgi.application"

{%- if cookiecutter.use_tailwind %}
# Theme
TAILWIND_APP_NAME = "{{ cookiecutter.initial_app_name }}.theme"
{%- endif %}

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Storage backend
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
