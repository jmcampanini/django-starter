import dj_database_url
from os import environ
from core.planeteer import load_the_environment


# #############################################################################
# SETUP ENVIRONMENT, PART 1
# #############################################################################
# Assume we're in the development environment
CLEAN_ENV = str(environ.get("ENV", "dev")).strip().lower()
load_the_environment(CLEAN_ENV, False)


# #############################################################################
# DEBUG SETTINGS
# #############################################################################
DEBUG = True
TEMPLATE_DEBUG = DEBUG


# #############################################################################
# DATABASE SETTINGS
# #############################################################################
DATABASES = {
	"default": dj_database_url.config(default="sqlite:///db.sqlite")
}


# #############################################################################
# TEMPLATES, MIDDLEWARE & WSGI
# #############################################################################
TEMPLATE_LOADERS = ("django.template.loaders.filesystem.Loader",
					"django.template.loaders.app_directories.Loader")

MIDDLEWARE_CLASSES = ("django.middleware.common.CommonMiddleware",
					  "django.contrib.sessions.middleware.SessionMiddleware",
					  "django.middleware.csrf.CsrfViewMiddleware",
					  "django.contrib.auth.middleware.AuthenticationMiddleware",
					  "django.contrib.messages.middleware.MessageMiddleware")

ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"


# #############################################################################
# APPS
# #############################################################################
INSTALLED_APPS = ("django.contrib.auth",
				  "django.contrib.contenttypes",
				  "django.contrib.sessions",
				  "django.contrib.sites",
				  "django.contrib.messages",
				  "django.contrib.staticfiles",
				  "django.contrib.admin",
				  "django.contrib.admindocs",

				  "debug_toolbar",
				  "storages",
				  "django_nose",
				  "djcelery")


# #############################################################################
# OTHER
# #############################################################################
SITE_ID = 1

ADMINS = ()
MANAGERS = ADMINS

USE_TZ = False
TIME_ZONE = "UTC"
LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_L10N = True

SECRET_KEY = "REPLACE_ME"


# #############################################################################
# APP SETTINGS
# #############################################################################
try: from settings_apps import *
except ImportError: pass


# #############################################################################
# SETUP ENVIRONMENT, PART 2
# #############################################################################
if CLEAN_ENV == "dev":
	print "DEV Environment"
	try: from settings_dev import *
	except ImportError: pass

elif CLEAN_ENV == "prod":
	print "PROD Environment"
	try: from settings_prod import *
	except ImportError: pass