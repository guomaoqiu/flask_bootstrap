from flask import render_template, abort, redirect
from . import main
from flask_login import current_user, login_required
from ..models import User
import os

@main.route('/')
def index():
    if not current_user.is_authenticated:
        print 'xxxxxxxxxxxxxxxxxxxxxxxx',os.environ.get('DB_PORT_3306_TCP_ADDR')
        return redirect('auth/login')
       
    else:
        #return 'TEST'
        return render_template('index.html')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)
