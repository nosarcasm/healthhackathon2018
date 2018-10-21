from medtracker import *
from medtracker.models import *
from medtracker.forms import *
from flask import flash, Markup
import random, string, math, datetime
import pytz

import flask_login
from flask_login import login_required
from flask_login import login_user, logout_user, current_user

def calc_food_stats(f):
	f.phe = f.nutr_508 if f.nutr_508!=None else ""
	f.ile = f.nutr_503 if f.nutr_503!=None else float('nan')
	f.leu = f.nutr_504 if f.nutr_504!=None else float('nan')
	f.val = f.nutr_510 if f.nutr_510!=None else float('nan')
	f.bcaa = round(float(f.ile)+float(f.leu)+float(f.val),2)
	f.bcaa = f.bcaa if math.isnan(f.bcaa)==False else ""
	return f

def calc_food_stats_units(f,quantity,weight):
	conv_factor = float(weight.gm_weight)/100.*float(quantity)
	fields = [a for a in f.__dict__.keys() if "nutr_" in a]
	for n in fields:
		orig_value = getattr(f,n)
		if orig_value != None:
			orig_value = float(orig_value)
			setattr(f,n,round(orig_value*conv_factor,2))
	return f


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
		f = calc_food_stats(f)
	return render_template("foods.html",foods=foods)

@app.route("/foods/search")
@login_required
def foods_search():
	search_term = request.values.get("search_term","")
	meal = request.values.get("meal","")
	if search_term != "":
		foods = Foods.query.filter(Foods.long_desc.contains(search_term)).all()
		for f in foods:
			f.str_pos = f.long_desc.lower().index(search_term.lower()) if search_term.lower() in f.long_desc.lower() else 99
			f = calc_food_stats(f)
		foods = sorted(foods,key=lambda f: f.str_pos)
	else:
		foods = []
	return render_template("foods_search.html",foods=foods,search_term=search_term,meal=meal)

@app.route("/foods/<ndb_id>/add", methods=['GET', 'POST'])
@login_required
def food_add(ndb_id):
	food = Foods.query.get_or_404(ndb_id)
	meal = request.values.get("meal","")
	formobj = FoodHistoryForm(request.form)
	formobj.units.query = food.weights.all()
	formobj.food_desc.data = food.long_desc
	formobj.day.data = datetime.datetime.now()
	if meal != "":
		formobj.meal.data = meal
	if request.method == 'POST' and formobj.validate():
		food_hist = FoodHistory(food.ndb_id,
		                        current_user.id,
		                        formobj.day.data,
						        formobj.meal.data,
						        formobj.quantity.data,
						        formobj.units.data.index)
		db.session.add(food_hist)
		db.session.commit()
		flash("Food added to history.")
		return redirect(url_for("food_daily_log"))
	return render_template("form.html",action="Add", data_type="food to your log", form=formobj)

@app.route("/foods/<int:ndb_id>")
@login_required
def food_view(ndb_id):
	food = Foods.query.get_or_404(ndb_id)
	food = calc_food_stats(food)
	return render_template("food_view.html",food=food)

@app.route("/foods/log")
@login_required
def food_daily_log():
	day = request.values.get("day","2018-10-21")
	breakfast = FoodHistory.query.filter_by(meal="Breakfast",day=day,user_id=current_user.id).all()
	lunch= FoodHistory.query.filter_by(meal="Lunch",day=day,user_id=current_user.id).all()
	dinner = FoodHistory.query.filter_by(meal="Dinner",day=day,user_id=current_user.id).all()
	snacks = FoodHistory.query.filter_by(meal="Snacks",day=day,user_id=current_user.id).all()
	for h in breakfast:
		h.food = calc_food_stats(calc_food_stats_units(h.food,h.quantity,h.weight))
	for h in lunch:
		h.food = calc_food_stats(calc_food_stats_units(h.food,h.quantity,h.weight))
	for h in dinner:
		h.food = calc_food_stats(calc_food_stats_units(h.food,h.quantity,h.weight))
	for h in snacks:
		h.food = calc_food_stats(calc_food_stats_units(h.food,h.quantity,h.weight))
	return render_template("food_daily_log.html",
	                       breakfast=breakfast,
	                       lunch=lunch,
	                       dinner=dinner,
	                       snacks=snacks)
@app.route("/foods/history/delete/<int:hist_id>")
@login_required
def delete_food_history(hist_id):
	history = FoodHistory.query.get_or_404(hist_id)
	db.session.delete(history)
	db.session.commit()
	flash("Food deleted.")
	return redirect(url_for("food_daily_log"))

@app.route("/plans")
@login_required
def plan_index():
	plans = Treatments.query.all()
	return render_template("meal_plans.html", plans = plans)

@app.route("/plans/view/<int:plan_id>", methods=["GET", "POST"])
@login_required
def plan_view(plan_id):
	plan = Treatments.query.get_or_404(plan_id)
	return render_template("plan_view.html",plan=plan)

@app.route("/plans/new", methods=["GET", "POST"])
@login_required
def plan_add():
	formobj = PlanForm()
	plan = Treatments()
	if request.method == 'POST' and formobj.validate():
		formobj.populate_obj(plan)
		db.session.add(plan)
		db.session.commit()
		flash("Plan added")
		return redirect(url_for("plan_index"))
	return render_template("form.html",action="Add", data_type="a meal plan", form=formobj)

@app.route("/plans/<int:plan_id>/add", methods=["GET", "POST"])
@login_required
def plan_add_treatments(plan_id):
	plan = Treatments.query.get_or_404(plan_id)
	formobj = PlanDetailForm()
	formobj.nutr_id.query = Nutrients.query.all()
	if request.method == 'POST' and formobj.validate():
		treatmentdetail = TreatmentDetail(treatment_id = plan.id,
									      nutr_id = formobj.nutr_id.data.nutr_id,
									      operator = formobj.operator.data,
									      value = formobj.value.data)
		db.session.add(treatmentdetail)
		db.session.commit()
		flash("Detail added")
		return redirect(url_for("plan_view",plan_id=plan.id))
	return render_template("form.html",action="Add", data_type="details to "+plan.title, form=formobj)

@app.route("/plan/details/delete/<int:treatdetail_id>")
@login_required
def delete_plan_detail(treatdetail_id):
	detail = TreatmentDetail.query.get_or_404(treatdetail_id)
	plan_id = detail.treatment.id
	db.session.delete(detail)
	db.session.commit()
	flash("Detail deleted.")
	return redirect(url_for("plan_view",plan_id=plan_id))

@app.route("/plans/delete/<int:plan_id>")
@login_required
def delete_plan(plan_id):
	plan = Treatments.query.get_or_404(plan_id)
	db.session.delete(plan)
	db.session.commit()
	flash("Plan deleted.")
	return redirect(url_for("plan_index"))

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
	return render_template('form_login.html', form=form, action="Please log in", data_type="",form_action="/login")

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
