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
# MEDIA & STATIC & TEMPLATES & MIDDLEWARE
# #############################################################################
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "__media/")
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(PROJECT_ROOT, "__static/")
STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "_staticfiles/"),)

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
					   "django.contrib.staticfiles.finders.AppDirectoriesFinder")

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "_templates/"),)

MIDDLEWARE_CLASSES = MWC + ("debug_toolbar.middleware.DebugToolbarMiddleware",)


# #############################################################################
# LOGGING
# #############################################################################
LOGGING = {
	"version": 1,
	"disable_existing_loggers": False,
	"formatters": {
		"verbose": {
			"format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
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
		#		"django.db.backends": {
		#			"handlers": ["console"],
		#			"level": "DEBUG",
		#			"propagate": True
		#		}
	}
}


# #############################################################################
# TEST SETTINGS
# #############################################################################
CELERY_ALWAYS_EAGER = True
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"