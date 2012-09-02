import os


# #############################################################################
# CELERY
# #############################################################################
import djcelery
djcelery.setup_loader()

BROKER_URL = os.environ.get("CLOUDAMQP_URL", "")

CELERYD_CONCURRENCY = 2