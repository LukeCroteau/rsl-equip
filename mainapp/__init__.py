'''
Main Flask App Initialization
'''
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from config import main_config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

MAIN_APPLICATION = Flask(__name__)
MAIN_APPLICATION.config.from_object(main_config)

engine = create_engine(main_config.DATABASE_URL, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

import mainapp.database

migrate = Migrate(MAIN_APPLICATION, Base)

LOGIN_MANAGER = LoginManager(MAIN_APPLICATION)

# Import all our Routes
from mainapp.Views.user_authentication import authentication_blueprint
from mainapp.Views.site_documentation import documentation_blueprint
from mainapp.Views.static_files import static_files_blueprint
from mainapp import main

MAIN_APPLICATION.register_blueprint(authentication_blueprint)
MAIN_APPLICATION.register_blueprint(documentation_blueprint, url_prefix='/documentation')
MAIN_APPLICATION.register_blueprint(static_files_blueprint)
