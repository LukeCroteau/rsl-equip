'''
Global Config
'''
import os
from dotenv import load_dotenv
from flask import session

class main_config:
    print('Loading Environment and Configuration')
    load_dotenv(verbose=True)

    EXPLAIN_TEMPLATE_LOADING = os.environ.get('EXPLAIN_TEMPLATE_LOADING')
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'sqlite:////config/test.db'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Secret'
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or 'Super Secret'
    GOOGLE_OAUTH_CLIENT = os.environ.get('GOOGLE_OAUTH_CLIENT_ID') or 'This is a secret key'
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET_ID') or 'This is another secret key'

    # oauth = OAuth()
    # google = oauth.remote_app(
    #         'google',
    #         consumer_key=GOOGLE_OAUTH_CLIENT,
    #         consumer_secret=GOOGLE_OAUTH_CLIENT_SECRET,
    #         request_token_params={
    #             'scope': 'email'
    #         },
    #         base_url='https://www.googleapis.com/oauth2/v1/',
    #         request_token_url=None,
    #         access_token_method='POST',
    #         access_token_url='https://accounts.google.com/o/oauth2/token',
    #         authorize_url='https://accounts.google.com/o/oauth2/auth',
    #     )

    # @google.tokengetter
    # def get_google_oauth_token():
    #     return session.get('google_token')

