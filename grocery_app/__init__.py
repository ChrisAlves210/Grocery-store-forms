from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from grocery_app.extensions import app, db
from grocery_app.models import User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

bcrypt = Bcrypt(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
