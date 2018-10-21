from medtracker import *
from medtracker.models import *
from medtracker.forms import *
from flask import flash, Markup
import random, string, math
import pytz

import flask_login
from flask_login import login_required
from flask_login import login_user, logout_user, current_user

@app.route("/")
def splash_page():
    return send_from_directory("/app/assets/","splash-page/index.html")

@app.route("/home")
@login_required
def index():
    return render_template("index.html")

@app.route('/assets/<path:path>')
def send_js(path):
    return send_from_directory('/app/assets', path)

@app.route("/foods")
@login_required
def foods_index():
	foods = Foods.query.all()
	for f in foods:
		f.phe = f.nutr_508 if f.nutr_508!=None else ""
		f.ile = f.nutr_503 if f.nutr_503!=None else float('nan')
		f.leu = f.nutr_504 if f.nutr_504!=None else float('nan')
		f.val = f.nutr_510 if f.nutr_510!=None else float('nan')
		f.bcaa = round(float(f.ile)+float(f.leu)+float(f.val),2)
		f.bcaa = f.bcaa if math.isnan(f.bcaa)==False else ""
	return render_template("foods.html",foods=foods)

@app.route("/foods/<int:ndb_id>")
@login_required
def food_view(ndb_id):
	food = Foods.query.get_or_404(ndb_id)
	'''
	for f in foods:
		f.carbs = f.nutrient_data.filter_by(nutr_id='205').first().nutr_value
		f.protein = f.nutrient_data.filter_by(nutr_id='203').first().nutr_value
		f.fats = f.nutrient_data.filter_by(nutr_id='204').first().nutr_value
		f.calories = f.nutrient_data.filter_by(nutr_id='208').first().nutr_value
		f.phe = f.nutrient_data.filter_by(nutr_id='508').first()
		f.phe = f.phe.nutr_value if f.phe!=None else 'N/D'
		f.ile = f.nutrient_data.filter_by(nutr_id='503').first()
		f.leu = f.nutrient_data.filter_by(nutr_id='504').first()
		f.val = f.nutrient_data.filter_by(nutr_id='510').first()
		f.bcaa = round(float(f.ile.nutr_value)+float(f.leu.nutr_value)+float(f.val.nutr_value),2) if (f.ile!=None)&(f.leu!=None)&(f.val!=None) else 'N/D'
	'''
	return render_template("food_view.html",food=food)

@app.route("/nutrients")
@login_required
def nutrients_index():
	nutrients = Nutrients.query
	return render_template("nutrients.html",nutrients=nutrients)

#### logins

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view =  "login"

@login_manager.user_loader
def user_loader(user_id):				# used by Flask internally to load logged-in user from session
	return User.query.get(user_id)

@app.route("/login", methods=["GET", "POST"])
@login_manager.unauthorized_handler
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
