""" Top level module

This module:

- Contains create_app()
- Registers extensions
"""

from flask import Flask

# Import extensions
from .extensions import bcrypt, cors, db, jwt, ma, admin, ModelView

# Import config
from config import config_by_name


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    register_extensions(app)

    # Register blueprints
    from .auth import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")

    from .api import api_bp
    app.register_blueprint(api_bp, url_prefix="/api", )
    
    from .pwa_blueprint import pwa_blueprint
    app.register_blueprint(pwa_blueprint, url_prefix="/pwa")
    
    from .app_blueprint import app_blueprint
    app.register_blueprint(app_blueprint)
     
    admin.name='boilerplate'
    admin.template_mode='bootstrap4'
    from app.models.user import User, Role
    
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session))

    return app


def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    admin.init_app(app)