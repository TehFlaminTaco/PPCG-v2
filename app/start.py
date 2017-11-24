import app.server

# noinspection PyUnresolvedReferences
# This statement needs to be here in order to link the routes.
# Since all the work is being done by the code in the routes modules being run,
# Nothing from the modules actually gets called from something external.
from app.routes import *

# Sets up authorization middleware.

# Sets up Celery connection

# Exports server to please Flask CLI
server = app.server.server


def run(host, port):
    app.server.server.run(host=host, port=port)
