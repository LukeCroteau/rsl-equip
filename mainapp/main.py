'''
Main program.
'''
from flask import render_template, redirect, url_for
from mainapp import db_session, MAIN_APPLICATION, LOGIN_MANAGER
from mainapp.database import init_db
from mainapp.data_import import import_static_data
from mainapp.Models.user_data import User

LOGIN_MANAGER.login_view = '/login'
LOGIN_MANAGER.login_message_category = 'warning'

@LOGIN_MANAGER.user_loader
def load_user(id):
    ''' Required by Login Manager '''
    return User.query.get(int(id))

@MAIN_APPLICATION.teardown_request
def shutdown_session(exception=None):
    ''' Required by SQLAlchemy '''
    db_session.remove()

@MAIN_APPLICATION.route('/')
def home():
    ''' Main Dashboard '''
    return render_template('pages/home.html')

@MAIN_APPLICATION.route('/initdb/54*Banana*54')
def database_init():
    init_db()
    return 'Databases Initialized'

@MAIN_APPLICATION.route('/createdb/54*Banana*54')
def quick_import():
    import_static_data()
    return 'Data Imported'

@MAIN_APPLICATION.errorhandler(500)
def internal_error(error):
    ''' Internal Error '''
    db_session.rollback()
    return render_template('errors/500.html'), 500

@MAIN_APPLICATION.errorhandler(404)
def not_found_error(error):
    ''' File not found '''
    return render_template('errors/404.html'), 404

if __name__ == '__main__':
    MAIN_APPLICATION.run(debug=True, host='0.0.0.0')
