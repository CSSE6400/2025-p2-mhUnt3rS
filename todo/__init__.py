from flask import Flask
from todo.models import db
from todo.models.todo import Todo
from .views.routes import api

def create_app(config_overrides=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite"
    
    if config_overrides:
        app.config.update(config_overrides)
    
    # Load the models
    db.init_app(app)
    
    # Create the database tables
    with app.app_context():
        db.create_all()
        db.session.commit()
    
    # Register the blueprints
    app.register_blueprint(api)
    
    return app

