# coding: utf-8
from medtracker import app #import init params like where the db is

from flask_sqlalchemy import * #import sql wrapper functions from Flask web helper lib
from sqlalchemy import orm, asc, desc #this is used to give SQLite properties to our Python classes

from passlib.apps import custom_app_context as pwd_context #encrypts password

db = SQLAlchemy(app) #create the db object in sqlalchemy

#float(f.weights.all()[1].gm_weight)/100.*float(f.nutrient_data.first().nutr_value)

class foods(db.Model):

    __tablename__='food_desc'

    ndb_id = db.Column(db.Text, primary_key=True)
    foodgroup_code = db.Column(db.Text)
    long_desc = db.Column(db.Text)
    short_desc = db.Column(db.Text)
    common_name = db.Column(db.Text)
    manufacturer_name = db.Column(db.Text)
    survey = db.Column(db.Text)
    ref_desc = db.Column(db.Text)
    ref_use = db.Column(db.Text)
    scientific_name = db.Column(db.Text)
    nit_factor = db.Column(db.Text)
    prot_factor = db.Column(db.Text)
    fat_factor = db.Column(db.Text)
    carb_factor = db.Column(db.Text)

    weights = db.relationship("food_weights",backref="food",lazy="dynamic")
    nutrient_data = db.relationship("food_nutrient_data",backref="food",lazy="dynamic")

    def __repr__(self):
        return "<Food(ndb_id='%s', long_desc='%s')"%(self.ndb_id,self.long_desc)

class nutrients(db.Model):
    __tablename__ = 'nut_def'

    nutr_id = db.Column(db.Text, primary_key=True)
    units = db.Column(db.Text)
    tagname = db.Column(db.Text)
    nutr_desc = db.Column(db.Text)
    num_decimal_pts = db.Column(db.Text)
    sr_order = db.Column(db.Text)

    data = db.relationship("food_nutrient_data",backref="nutrient",lazy="dynamic")

    def __repr__(self):
        return "<Nutrient(nutr_id='%s', nutr_desc='%s')"%(self.nutr_id,self.nutr_desc)

class food_weights(db.Model):

    __tablename__ = 'food_meas'

    index = db.Column(db.BigInteger, primary_key=True)
    ndb_id = db.Column(db.Text,db.ForeignKey('food_desc.ndb_id'))
    seq = db.Column(db.Text)
    amount = db.Column(db.Text)
    measure_desc = db.Column(db.Text)
    gm_weight = db.Column(db.Text)
    num_data_pts = db.Column(db.Text)
    std_dev = db.Column(db.Text)

    def __repr__(self):
        return "<Weight(index='%s', measure_desc='%s')"%(self.index,self.measure_desc)


class food_nutrient_data(db.Model):

    __tablename__ = 'nut_data'

    index = db.Column(db.BigInteger, primary_key=True)
    ndb_id = db.Column(db.Text, db.ForeignKey('food_desc.ndb_id'))
    nutr_id = db.Column(db.Text, db.ForeignKey('nut_def.nutr_id'))
    nutr_value = db.Column(db.Text)
    num_data_pts = db.Column(db.Text)
    std_err = db.Column(db.Text)
    src_code = db.Column(db.Text)
    deriv_code = db.Column(db.Text)
    ref_ndb_no = db.Column(db.Text)
    add_nutr_mark = db.Column(db.Text)
    num_studies = db.Column(db.Text)
    min_val = db.Column(db.Text)
    max_val = db.Column(db.Text)
    deg_freedom = db.Column(db.Text)
    low_eb = db.Column(db.Text)
    up_eb = db.Column(db.Text)
    stat_cmt = db.Column(db.Text)
    addmod_date = db.Column(db.Text)

    def __repr__(self):
        return "<NutrientData(index='%s', value='%s')"%(self.index,
                                                        self.nutr_value)

class User(db.Model):
    """A user capable of eating foods"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    password_hash = db.Column(db.String(256))
    authenticated = db.Column(db.Boolean, default=False)
    
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the id to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    """TODO
    have many foodhistory
    have many diseasehistory
    have many symptomhistory
    have many medicationhistory
    """

""" 
# MORE TODO 10/19/18

## we need a way to add custom foods and allow users to specify nutrients

class FoodHistory(db.Model):
    ##TODO
    belongs_to user

class Disease(db.Model):
    ##TODO
    have many symptoms
    have many treatments
    join with diseasehistory

class DiseaseHistory(db.Model):
    ##TODO
    belongs to user
    join with diease
    time_dx

class Symptoms(db.Model):
    ##TODO
    belongs to many diseases
    name

class SymptomHistory(db.Model):
    ##TODO
    belongs to patient
    join with symptoms
    time_had

class Medications(db.Model):
    ##TODO
    join with medicationhistory

class MedicationHistory(db.Model):
    ##TODO
    belongs to patient
    join with medication
    time_had

class Treatments(db.Model):
    ##TODO
    '''named treatments for disease'''
    has many diseases
    treatmentdetail
    name_of_treatment

class TreatmentDetail(db.Model):
    ##TODO
    belongs_to treatment
    treatment id (joins)
    value
    operator (<,==,>)
    units (%, g, mg, etc.)

"""