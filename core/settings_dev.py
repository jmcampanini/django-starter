import os
from core.settings import MIDDLEWARE_CLASSES as MWC


PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..")


# #############################################################################
# DEBUG SETTINGS
# #############################################################################
DEBUG = True

INTERNAL_IPS = ("127.0.0.1",)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False
}


# #############################################################################
# EMAIL SETTINGS
# #############################################################################
# Use a local host: python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False


# #############################################################################
# CACHE SETTINGS
# #############################################################################
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache"
    }
}


# #############################################################################
# MEDIA & STATIC & TEMPLATES & MIDDLEWARE
# #############################################################################
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "__media/")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(PROJECT_ROOT, "__static/")
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "_staticfiles/"),)

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder")

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "_templates/"),)

MIDDLEWARE_CLASSES = MWC + (
    "debug_toolbar.middleware.DebugToolbarMiddleware",)


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
        },
        #        "django.db.backends": {
        #            "handlers": ["console"],
        #            "level": "DEBUG",
        #            "propagate": True
        #        }
    }
}


# #############################################################################
# TEST SETTINGS
# #############################################################################
CELERY_ALWAYS_EAGER = True
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
