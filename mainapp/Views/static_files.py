'''
Static File Endpoints
'''

from flask import render_template, Blueprint, current_app, send_from_directory, request

static_files_blueprint = Blueprint('static_files', __name__, template_folder='templates')

@static_files_blueprint.route('/robots.txt')
def static_from_root():
    ''' Send the Robots file '''
    return send_from_directory(current_app.static_folder, request.path[1:])


