from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# Initialize the database object
db = SQLAlchemy()

def create_app():
    # Create the Flask application
    app = Flask(__name__)
    
    # Set the database URI (SQLite example)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postrges@localhost:5432/flaskdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'SOME KEY'

    login_manager = LoginManager()
    login_manager.init_app(app)

    from dbmodels import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    bcrypt = Bcrypt(app)

    # Initialize the database with the app
    db.init_app(app)

    # Initialize Flask-Migrate with the app and db
    migrate = Migrate(app, db)

    # Import and register routes
    from dbroutes import register_routes
    register_routes(app, db, bcrypt)

    return app
