import os

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            #"format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "format": "{levelname} {asctime} {process:d} [{app_label}.{classname}] {funcName} - {message}",
            "style": "{",
            'defaults': {
                'app_label': '{{ cookiecutter.project_slug }}',
                'classname': 'Unknown',
            }
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console_simple": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "console_verbose": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console_simple"],
        "level": "WARNING",
    },
    "loggers": {
        "django": {
            "handlers": ["console_simple"],
            "level": "INFO",
            "propagate": False,
        },
        "core.models": {
            "handlers": ["console_verbose"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}
