django-starter
==============

A starting template for a heroku-compatible Django project.


## Key Capabilities
- Procfile ready for Heroku deployment
- Environments using `.env` files. See `.env.sample` template to get started.
- Uses Database URLs and Heroku PostgreSQL in production, and `sqlite` in development.
- Production settings using `django-storages` & Amazon S3 for assets.
- Testing using `debug-toolbar` and `django-nose`.
- Email settings using MailGun `ENV` variables (commented out initially).
- Cache settings for development & production
- Celery configuration using CloudAMQP on heroku, and eager tasks locally (no broker)
- South included for database migrations
- PEP8 Support

## Included Components
- Python/Django
	- Django
	- gunicorn
	- south
	- PEP8
- Testing
	- django-debug-toolbar
	- sure
	- django-nose
- Heroku Compatability
	- dj-database-url
	- psycopg2
	- django-storages
	- boto
	- celery
	- pylibmc
	- New Relic
- HTML/CSS
	- Bootstrap 2.2.2
	- jQuery 1.8.3
	- Font Awesome 3.0.0
	- [eternicode / bootstrap-datepicker](https://github.com/eternicode/bootstrap-datepicker)
	- [eldarion / bootstrap-ajax](https://github.com/eldarion/bootstrap-ajax)


## To Begin
1. Setup a virtual environment & install the python dependencies
	1. `virtualenv [ENVIRONMENT_NAME]`
	2. `pip install -r requirements.txt`
2. Update the `SECRET_KEY` variable in the `core/settings.py` file - [django secret key generator](http://www.miniwebtool.com/django-secret-key-generator/).
3. Remove `core/_delete_me.py` and update the `core/url.py` file.


## To Deploy to Heroku
- First-time Deployments:
	1. Create the application: `heroku create [APP_NAME]`
	2. Enable ENV variables during compile: `heroku labs:enable user-env-compile`
	3. Install the Heroku Add Ons you will be using.
- Updates
	1. If needed, push up the local `.env` file: `heroku config:push`
	2. Push the latest version to heroku: `git push heroku master`
	3. Sync the DB: `heroku run python manage.py syncdb`
	4. Collect Static Files to Amazaon S3: `heroku run python manage.py collectstatic`


## Directory Structure
- `django-starter`
	- `__static/` - local directory used as the `STATIC_ROOT`. not used in production.
	- `__media/` - local directory used as the `MEDIA_ROOT`. not used in production.
	- `_staticfiles/` - static files.
		- `css` - compiled LESS files are placed here.
		- `font` - fonts for Font Awesome.
		- `js` - jquery and bootstrap plug-ins.
		- `less` - assets for Bootstrap.
	- `_templates/` - primary template directory
	- `_vendor/` - contains vendor-specific README, license information, etc.
	- `core/` - project directory
		- `settings.py` - common settings. loads other settings files.
		- `settings_apps.py` - specific settings for applications (i.e., celery, etc.).
		- `settings_dev.py` - settings for local development.
		- `settings_prod.py` - settings for a production deployment (on heroku).
		- `urls.py`
	- `.env.sample` - a sample `.ENV` file, with the fields needed in production.
	- `Procfile` - heroku compatability
	- `requirements.txt`
	- `manage.py`


## Environments
There are 2 primary environments:

- **DEV** - `dev` - Local, testing/development environment on a developer's computer. (Default).
- **PROD** - `prod` - In-the-cloud deployment, on Heroku.

Which environment the app is in is determined by an environment variable: `ENV`. **It defaults to the DEV environment**.

Given which environment, the project will do the following:

- Load the `.env` (for production) or `.env.dev` (for development) file into the python environment dictionary.
- Load the `settings_[ENV].py` file with the appropriate settings.


## Heroku Addon Capabilities
- Currently supported:
	- Heroku Postgres
	- Mailgun
	- CloudAMQP
	- MemCachier
	- New Relic


## Upcoming Features
- Multiple Environments (Staging, Clones)
- Heroku Automation
- Pre-Deployment Asset Processing
- Deployment Automation
- CDN Support


# External Dependencies (optional)
- Homebrew - see `.brew` file for packages
- Less Compiler - Mac OS X - [Less.app](http://incident57.com/less/)
