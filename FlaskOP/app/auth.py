from app import basic_auth
from app.models.user import User
from werkzeug.security import check_password_hash

@basic_auth.verify_password
def verify_password(email, password):
    user = User.query.filter_by(email=email).first()

    if not user:
        return False
    return check_password_hash(user.password, password)