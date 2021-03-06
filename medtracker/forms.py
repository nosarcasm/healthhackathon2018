from wtforms import *
from flask_wtf import Form
from wtforms.ext.sqlalchemy.fields import *
from wtforms.fields.html5 import DateField, DecimalRangeField
from wtforms.validators import DataRequired
from flask.views import MethodView
import re

from medtracker.models import *

class DisabledTextField(TextField):
  def __call__(self, *args, **kwargs):
    kwargs.setdefault('disabled', True)
    return super(DisabledTextField, self).__call__(*args, **kwargs)

class DisabledSelectField(SelectField):
  def __call__(self, *args, **kwargs):
    kwargs.setdefault('disabled', True)
    return super(DisabledSelectField, self).__call__(*args, **kwargs)

class UsernamePasswordForm(Form):
    username = StringField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class NewUserForm(Form):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Full Name', validators=[DataRequired()])

class FoodHistoryForm(Form):				
    food_desc = DisabledTextField('Name')
    day = DateField('Day consumed')
    meal = SelectField('Meal', choices=[("Breakfast","Breakfast")
                       ,("Lunch","Lunch"),
                       ("Dinner","Dinner"),
                       ("Snacks","Snacks")])
    units = QuerySelectField("Serving size", 
		get_pk=lambda a: a.index, get_label=lambda a: a.measure_desc)
    quantity = FloatField("Number of servings")

class PlanForm(Form):
	title = TextField("Title")
	description = TextField("Description")

class PlanDetailForm(Form):				
    nutr_id = QuerySelectField("Nutrient", 
		get_pk=lambda a: a.nutr_id, get_label=lambda a: a.nutr_desc+" ("+a.units+")")
    operator = SelectField('Criteria', choices=[("<","less than")
                       ,("<=","less than or equal to"),
                       ("==","equals"),
                       (">","greater than"),
                       (">=","greater than or equal to")])
    value = FloatField("Value")

class SymptomForm(Form):
	name = TextField("Name")
	day = DateField('Day occurred')
	value = DecimalRangeField("Severity", {"min":0,"max":10})
