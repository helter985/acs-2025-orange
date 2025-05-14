from flask import Flask
from flask_cors import CORS
from app.config.database import *
from flask_migrate import Migrate
from app.models import *
from flask_marshmallow import Marshmallow

def create_app():
    app = Flask(__name__)
    ma = Marshmallow()
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
 
    from app.controllers import  product
    app.register_blueprint(product, url_prefix='/api/v1')

    return app