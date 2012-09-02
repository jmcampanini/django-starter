import os


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
#EMAIL_USE_TLS = string_to_bool(os.environ.get("EMAIL_USE_TLS", "True"), default=True)


# #############################################################################
# AWS S3
# #############################################################################
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_BUCKET")
AWS_S3_SECURE_URLS = False


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

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.FileSystemFinder",
					   "django.contrib.staticfiles.finders.AppDirectoriesFinder")

TEMPLATE_DIRS = ("_templates/",)


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
		}
	}
}