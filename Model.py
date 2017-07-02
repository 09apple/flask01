from sqlalchemy.testing import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):

    # password_hash = db.Column(db.String(128))

    @property
    def password(self):
        pass


