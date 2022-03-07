from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import  FileStorage

bootstrap = Bootstrap()
db = SQLAlchemy()

mail = Mail()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)

def create_app(config_name):

    app = Flask(__name__)
    

    mail.init_app(app)
    
    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)
    db.init_app(app)

    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # Will add the views and forms

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #Initializing flasks extensions
    # bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # configure UploadSet
    configure_uploads(app,photos)



    return app
