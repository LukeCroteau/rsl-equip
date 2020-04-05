'''
Site Documentation Endpoints
'''

from flask import render_template, Blueprint

documentation_blueprint = Blueprint('site_documentation', __name__, template_folder='templates')

@documentation_blueprint.route('/about')
def about():
    ''' About Page '''
    return render_template('pages/about.html')

