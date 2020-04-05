'''
User Authentication Endpoints
'''

from flask import render_template, Blueprint, session, url_for, redirect
from flask import current_app as app
from flask_login import login_user, logout_user, current_user
from config import main_config
from mainapp.Models.user_data import User
from mainapp import db_session

authentication_blueprint = Blueprint('authentication', __name__, template_folder='templates')

@authentication_blueprint.route('/login')
def login():
    ''' Login Page '''
    if 'google_token' in session:
        return redirect(url_for('authentication.google_oauth_login'))
    else:
        return render_template('pages/login.html')

@authentication_blueprint.route('/login_google')
def login_google():
        main_config.oauth.init_app(app)
        return main_config.google.authorize(callback=url_for('authentication.google_oauth_login', _external=True))

@authentication_blueprint.route('/google_oauth_login')
def google_oauth_login():
    ''' Handle a Google Login '''
    if 'google_token' not in session:
        resp = main_config.google.authorized_response()
        if resp is None:
            return 'Access denied: reason=%s error=%s' % (
                request.args['error_reason'],
                request.args['error_description']
            )

        session['google_token'] = (resp['access_token'], '')

    do_login_for_user(main_config.google.get('userinfo'))    
    return redirect(url_for('home'))
   
@authentication_blueprint.route('/logout')
def logout():
    ''' Log Out the current user '''
    do_logout_for_user()
    return redirect(url_for('home'))

def do_login_for_user(userinfo):
    ''' Handle the finding of the User record, and adding to the session '''
    user = User.query.filter(User.google_id == userinfo.data.get('id')).first()
    if not user:
        user = User(userinfo.data.get('given_name'), userinfo.data.get('family_name'), userinfo.data.get('name'), userinfo.data.get('email'), 
                    userinfo.data.get('gender'), userinfo.data.get('id'), userinfo.data.get('link'), userinfo.data.get('picture'))
        db_session.add(user)
        db_session.commit()
    login_user(user)

def do_logout_for_user():
    ''' Clear out User data from the session '''
    session.pop('google_token', None)
    logout_user()

