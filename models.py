from sqlalchemy import Column, Integer, String, Boolean

from db import Base, engine

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), index=True, unique=True)
    password = Column(String(128))
    role = Column(String(10), index=True)
    email = Column(String, unique=True)
    telegram_id = Column(Integer)
    is_teacher = Column(Boolean, unique=False, default=True)


    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)    

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User> {}'.format(self.username)

class Teachers_Students(Base):
    __tablename__ = 'teacher_students'
    id_student = relationship('User', lazy='joined')
    id_teacher = relationship('User', lazy='joined')

    def __repr__(self):
        return f'Student_id: {self.id_student}, Teacher_id: {self.id_teacher}'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)


