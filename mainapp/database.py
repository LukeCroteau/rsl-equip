'''
Main Database import module
'''
from mainapp import Base

print('Initializing Database Variables')

from mainapp.Models.user_data import User

def init_db():
    '''
    Import all modules here that might define models so that
    they will be registered properly on the metadata.  Otherwise
    you will have to import them first before calling init_db()
    '''
    Base.metadata.create_all(bind=engine)

