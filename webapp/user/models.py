import enum

from flask_login import UserMixin
from sqlalchemy.sql.schema import ForeignKey
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

    __table_args__ = (db.UniqueConstraint('id_student', 'id_teacher')) # мб не совсем верно

class Test_status(enum.Enum):
    APPROVE='approve'
    PUBLISHED='published'
    SWITCHOFF='switch_off'

class Test_type(enum.Enum):
    COUNTER_WORK='counter_work'
    VERIFICATION_WORK='verification_work'
    INDEPENDENT_WORK='independent_work'
    HOMEWORK='homework'

class Test(db.Model):
    __tablename__ == 'tests'

    id_test = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True)
    status = db.Column(db.Enum(Test_status), nullable=False, default=Test_status.PUBLISHED.value)
    id_teacher = db.Column(Integer, ForeignKey(User.id), index=True, nullable=False)
    five = db.Column(Integer)
    four = db.Column(Integer)
    three = db.Column(Integer)
    test_type = db.Column(db.Enum(Test_type), nullable=False, default=Test_type.INDEPENDENT_WORK.value)




  