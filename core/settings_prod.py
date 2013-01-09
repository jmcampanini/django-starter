import os
from datetime import datetime, timedelta


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")


# #############################################################################
# DEBUG SETTINGS
# #############################################################################
DEBUG = False


# #############################################################################
# EMAIL SETTINGS
# #############################################################################
#EMAIL_HOST = os.environ.get("MAILGUN_SMTP_SERVER", "")
#EMAIL_PORT = os.environ.get("MAILGUN_SMTP_PORT", "")
#EMAIL_HOST_USER = os.environ.get("MAILGUN_SMTP_LOGIN", "")
#EMAIL_HOST_PASSWORD = os.environ.get("MAILGUN_SMTP_PASSWORD", "")
#EMAIL_USE_TLS = string_to_bool(os.environ.get("EMAIL_USE_TLS", "True"),
#                               default=True)


# #############################################################################
# CACHE SETTINGS
# #############################################################################
os.environ["MEMCACHE_SERVERS"] = os.environ.get("MEMCACHIER_SERVERS", "")
os.environ["MEMCACHE_USERNAME"] = os.environ.get("MEMCACHIER_USERNAME", "")
os.environ["MEMCACHE_PASSWORD"] = os.environ.get("MEMCACHIER_PASSWORD", "")

CACHES = {
    "default": {
        "BACKEND": "django_pylibmc.memcached.PyLibMCCache",
        "LOCATION": os.environ.get("MEMCACHIER_SERVERS", ""),
        "TIMEOUT": 500,
        "BINARY": True
    }
}


# #############################################################################
# AWS S3
# #############################################################################
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_BUCKET")
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False

future = datetime.now() + timedelta(days=10)
AWS_HEADERS = {
    "Expires": future.strftime("%a, %d %b %Y %H:%M:%S GMT"),
    "Cache-Control": "max-age=86400, public"
}


# #############################################################################
# MEDIA & STATIC & TEMPLATES
# #############################################################################
MEDIA_ROOT = ""
MEDIA_URL = ""

STATIC_ROOT = ""
STATIC_URL = "http://s3.amazonaws.com/%s/" % AWS_STORAGE_BUCKET_NAME
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "_staticfiles/"),)

DEFAULT_FILE_STORAGE = "storages.backends.s3boto.S3BotoStorage"
STATICFILES_STORAGE = "storages.backends.s3boto.S3BotoStorage"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder")

TEMPLATE_DIRS = ("_templates/",)


# #############################################################################
# LOGGING
# #############################################################################
verbose_format = "%(levelname)s " +\
                 "%(asctime)s " +\
                 "%(module)s " +\
                 "%(process)d " +\
                 "%(thread)d " +\
                 "%(message)s"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": verbose_format
        }
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": True
        }
    }
}
