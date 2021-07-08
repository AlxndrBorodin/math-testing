from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.db import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    name = db.Column(db.String(50), index=True)
    surname = db.Column(db.String(50), index=True)
    email = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User name={} id={}>'.format(self.username, self.id)

class Teacher_students(db.Model, UserMixin):
    __tablename__ = 'teachers_students'

    id_student = db.Column(Integer, ForeignKey(User.id), index=True, nullable=False)
    id_teacher = db.Column(Integer, ForeignKey(User.id), index=True, nullable=False)


  