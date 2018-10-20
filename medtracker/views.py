from medtracker import *
from medtracker.models import *
from medtracker.forms import *
from flask import flash, Markup
import random, string
import pytz

import flask_login
from flask_login import login_user, logout_user, current_user

@app.route("/")
def index():
    return send_from_directory("/app/assets/","splash-page/index.html")

@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('/app/assets', path)

#### logins

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "login"

@login_manager.user_loader
def user_loader(user_id):				# used by Flask internally to load logged-in user from session
	return User.query.get(user_id)

@login_manager.unauthorized_handler
@app.route("/login", methods=["GET", "POST"])
def login():					# not logged-in callback
	form = UsernamePasswordForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.username.data).first()
		if user == None:
			return str("Error: '" + form.username.data + "'")
		elif user.verify_password(form.password.data):
			login_user(user)
			return redirect(url_for('index'))
		else:
			return redirect(url_for('login'))
	return render_template('form_login.html', form=form, action="Please log in", data_type="")

@app.route('/logout')
def signout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = NewUserForm()
    if form.validate_on_submit():
        user = User(
            email = form.email.data,
            username = form.username.data,
            name = form.name.data,
        )
        user.hash_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template('form_signup.html', form=form, action="Sign up for Demeter", data_type="")

### end logins
