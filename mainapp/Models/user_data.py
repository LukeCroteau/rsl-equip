'''
User data schemas
'''
from sqlalchemy import Column, Integer, String, Boolean
from mainapp.database import Base

class User(Base):
    ''' Base class for User data '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    full_name = Column(String, index=True)
    gender = Column(String)
    google_id = Column(String, unique=True, index=True)
    google_link = Column(String)
    google_picture = Column(String)
    is_admin = Column(Boolean)
    is_maintainer = Column(Boolean)

    def __init__(self, first_name=None, last_name=None, full_name=None, email=None, gender=None, google_id=None,
                 google_link=None, google_picture=None):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.email = email
        self.gender = gender
        self.google_id = google_id
        self.google_link = google_link
        self.google_picture = google_picture
        self.is_admin = False
        self.is_maintainer = False

    def __repr__(self):
        return '<User %r>' % (self.email)

    ''' Flask-Login functions '''
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def can_upload(self):
        return (self.is_admin or self.is_maintainer)

    def is_administrator(self):
        return self.is_admin

    def get_id(self):
        return self.id
    ''' /Flask-Login functions '''
        