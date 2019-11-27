# We’re going to configure Flask, Connexion, SQLAlchemy, and Marshmallow here.

import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# basedir = 'c:\\dev\\flaskagain' in this case
basedir = os.path.abspath(os.path.dirname(__file__))


# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)

# Get the underlying Flask app instance
app = connex_app.app

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True # Useful for debugging only
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'people.db') # IN THE TUTORIAL THIS SQLITE PATH CONTAINS 4 SLASHES (////), IT HAS TO BE 3 DUE TO AN UPDATE (///)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Only useful for 'event-driven programs'

# Create the SQLAlchemy database instance
db = SQLAlchemy(app) # app = flask app instance

# Initialize Marshmallow
ma = Marshmallow(app)

