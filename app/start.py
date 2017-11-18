from app.server import server
from app.instances.db import db, redis_db
from app.models import *

# noinspection PyUnresolvedReferences
# This statement needs to be here in order to link the routes.
# Since all the work is being done by the code in the routes modules being run,
# Nothing from the modules actually gets called from something external.
from app.routes import *

# Sets up authorization middleware.
from app.instances import auth

# Sets up Celery connection
from app.helpers import tasks


def run(host, port):
    tasks.init.delay()
    server.run(host=host, port=port)
