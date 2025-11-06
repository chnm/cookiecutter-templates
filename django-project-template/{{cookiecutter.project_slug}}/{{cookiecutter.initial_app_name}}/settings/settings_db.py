from .settings import *

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
{% if cookiecutter.database == 'sqlite' %}
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
{% elif cookiecutter.database == 'postgres' %}
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
        "NAME": env("DB_NAME", default="{{ cookiecutter.project_slug }}"),
        "USER": env("DB_USER", default="{{ cookiecutter.project_slug }}"),
        "PASSWORD": env("DB_PASS", default="password"),
        "OPTIONS": {
            "options": "-c search_path=public"
        },
    },
    "test_app1_db": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": env("DB_HOST", default="localhost"),
        "PORT": env("DB_PORT", default="5432"),
        "NAME": env("DB_NAME", default="{{ cookiecutter.project_slug }}"),
        "USER": env("DB_USER", default="{{ cookiecutter.project_slug }}"),
        "PASSWORD": env("DB_PASS", default="password"),
        "OPTIONS": {
            "options": "-c search_path=test_app1"
        },
    },
{% endif %}
}

DATABASE_ROUTERS = [
    'test_app1.routers.DatabaseRouter',

    '{{ cookiecutter.initial_app_name }}.routers.db.AdminRouter',
    '{{ cookiecutter.initial_app_name }}.routers.db.DefaultRouter',
]
