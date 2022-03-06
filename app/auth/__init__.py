from flask import Blueprint
auth = Blueprint('auth',__name__)
from . import views,forms
from flask_uploads import UploadSet
# from werkzeug import secure_filename,FileStorage
from flask_migrate import Migrate, MigrateCommand