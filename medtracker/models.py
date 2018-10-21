# coding: utf-8
from medtracker import app #import init params like where the db is

from flask_sqlalchemy import * #import sql wrapper functions from Flask web helper lib
from sqlalchemy import orm, asc, desc #this is used to give SQLite properties to our Python classes

from passlib.apps import custom_app_context as pwd_context #encrypts password

db = SQLAlchemy(app) #create the db object in sqlalchemy

#copypasta from https://stackoverflow.com/questions/6587879/how-to-elegantly-check-the-existence-of-an-object-instance-variable-and-simultan
def get_or_create(model, **kwargs):
    '''get_or_create()

    Description: checks to see if an object with those properties exists in the db
    and returns it if it exists, otherwise returns a new object
    instantiated with the search **kwargs

    Inputs:
        model
            an empty instance of a class that inherits from sqlalchemy.model (e.g. class PersistentMedication(db.Model)).
            This should work with any class in this file.
        **kwargs
            filters for the database on that model when checking if an object exists already.
            For example, if we pass pricetable_id=12345 in the keyword arguments,
            it will return the first item of class *model* from the database that
            matches pricetable_id=12345 (e.g. the first PersistentMedication record).

    Returns:
        object
            The class object that was either found from the database or instantiated with **kwargs.
            This always returns an object the same class as the input *model*.
        found
            A boolean that denotes whether we found an object in the database (GET) or are
            instantiating it (CREATE). True if GET, False if CREATE.
    '''
    try:
        object = db.session.query(model).filter_by(**kwargs).first() #check if the object of class model exists in db
                                                                        #filtered on kwargs criteria and return the first match
        assert object != None #check if we got an object back
        return object, object != None
    except AssertionError:
        object = model(**kwargs) #return a blank object instatiated with kwargs if not found
        return object, False #set found to false

class Foods(db.Model):

    __tablename__='food_desc_full'

    ndb_id = db.Column(db.Text, primary_key=True)
    foodgroup_code = db.Column(db.Text)
    long_desc = db.Column(db.Text)
    short_desc = db.Column(db.Text)
    common_name = db.Column(db.Float)
    manufacturer_name = db.Column(db.Float)
    survey = db.Column(db.Text)
    ref_desc = db.Column(db.Float)
    ref_use = db.Column(db.Text)
    scientific_name = db.Column(db.Float)
    nit_factor = db.Column(db.Text)
    prot_factor = db.Column(db.Text)
    fat_factor = db.Column(db.Text)
    carb_factor = db.Column(db.Text)
    nutr_203 = db.Column(db.Float)
    nutr_204 = db.Column(db.Float)
    nutr_205 = db.Column(db.Float)
    nutr_207 = db.Column(db.Float)
    nutr_208 = db.Column(db.Float)
    nutr_209 = db.Column(db.Float)
    nutr_210 = db.Column(db.Float)
    nutr_211 = db.Column(db.Float)
    nutr_212 = db.Column(db.Float)
    nutr_213 = db.Column(db.Float)
    nutr_214 = db.Column(db.Float)
    nutr_221 = db.Column(db.Float)
    nutr_255 = db.Column(db.Float)
    nutr_262 = db.Column(db.Float)
    nutr_263 = db.Column(db.Float)
    nutr_268 = db.Column(db.Float)
    nutr_269 = db.Column(db.Float)
    nutr_287 = db.Column(db.Float)
    nutr_291 = db.Column(db.Float)
    nutr_301 = db.Column(db.Float)
    nutr_303 = db.Column(db.Float)
    nutr_304 = db.Column(db.Float)
    nutr_305 = db.Column(db.Float)
    nutr_306 = db.Column(db.Float)
    nutr_307 = db.Column(db.Float)
    nutr_309 = db.Column(db.Float)
    nutr_312 = db.Column(db.Float)
    nutr_313 = db.Column(db.Float)
    nutr_315 = db.Column(db.Float)
    nutr_317 = db.Column(db.Float)
    nutr_318 = db.Column(db.Float)
    nutr_319 = db.Column(db.Float)
    nutr_320 = db.Column(db.Float)
    nutr_321 = db.Column(db.Float)
    nutr_322 = db.Column(db.Float)
    nutr_323 = db.Column(db.Float)
    nutr_324 = db.Column(db.Float)
    nutr_325 = db.Column(db.Float)
    nutr_326 = db.Column(db.Float)
    nutr_328 = db.Column(db.Float)
    nutr_334 = db.Column(db.Float)
    nutr_337 = db.Column(db.Float)
    nutr_338 = db.Column(db.Float)
    nutr_341 = db.Column(db.Float)
    nutr_342 = db.Column(db.Float)
    nutr_343 = db.Column(db.Float)
    nutr_344 = db.Column(db.Float)
    nutr_345 = db.Column(db.Float)
    nutr_346 = db.Column(db.Float)
    nutr_347 = db.Column(db.Float)
    nutr_401 = db.Column(db.Float)
    nutr_404 = db.Column(db.Float)
    nutr_405 = db.Column(db.Float)
    nutr_406 = db.Column(db.Float)
    nutr_410 = db.Column(db.Float)
    nutr_415 = db.Column(db.Float)
    nutr_417 = db.Column(db.Float)
    nutr_418 = db.Column(db.Float)
    nutr_421 = db.Column(db.Float)
    nutr_428 = db.Column(db.Float)
    nutr_429 = db.Column(db.Float)
    nutr_430 = db.Column(db.Float)
    nutr_431 = db.Column(db.Float)
    nutr_432 = db.Column(db.Float)
    nutr_435 = db.Column(db.Float)
    nutr_454 = db.Column(db.Float)
    nutr_501 = db.Column(db.Float)
    nutr_502 = db.Column(db.Float)
    nutr_503 = db.Column(db.Float)
    nutr_504 = db.Column(db.Float)
    nutr_505 = db.Column(db.Float)
    nutr_506 = db.Column(db.Float)
    nutr_507 = db.Column(db.Float)
    nutr_508 = db.Column(db.Float)
    nutr_509 = db.Column(db.Float)
    nutr_510 = db.Column(db.Float)
    nutr_511 = db.Column(db.Float)
    nutr_512 = db.Column(db.Float)
    nutr_513 = db.Column(db.Float)
    nutr_514 = db.Column(db.Float)
    nutr_515 = db.Column(db.Float)
    nutr_516 = db.Column(db.Float)
    nutr_517 = db.Column(db.Float)
    nutr_518 = db.Column(db.Float)
    nutr_521 = db.Column(db.Float)
    nutr_573 = db.Column(db.Float)
    nutr_578 = db.Column(db.Float)
    nutr_601 = db.Column(db.Float)
    nutr_605 = db.Column(db.Float)
    nutr_606 = db.Column(db.Float)
    nutr_607 = db.Column(db.Float)
    nutr_608 = db.Column(db.Float)
    nutr_609 = db.Column(db.Float)
    nutr_610 = db.Column(db.Float)
    nutr_611 = db.Column(db.Float)
    nutr_612 = db.Column(db.Float)
    nutr_613 = db.Column(db.Float)
    nutr_614 = db.Column(db.Float)
    nutr_615 = db.Column(db.Float)
    nutr_617 = db.Column(db.Float)
    nutr_618 = db.Column(db.Float)
    nutr_619 = db.Column(db.Float)
    nutr_620 = db.Column(db.Float)
    nutr_621 = db.Column(db.Float)
    nutr_624 = db.Column(db.Float)
    nutr_625 = db.Column(db.Float)
    nutr_626 = db.Column(db.Float)
    nutr_627 = db.Column(db.Float)
    nutr_628 = db.Column(db.Float)
    nutr_629 = db.Column(db.Float)
    nutr_630 = db.Column(db.Float)
    nutr_631 = db.Column(db.Float)
    nutr_636 = db.Column(db.Float)
    nutr_638 = db.Column(db.Float)
    nutr_639 = db.Column(db.Float)
    nutr_641 = db.Column(db.Float)
    nutr_645 = db.Column(db.Float)
    nutr_646 = db.Column(db.Float)
    nutr_652 = db.Column(db.Float)
    nutr_653 = db.Column(db.Float)
    nutr_654 = db.Column(db.Float)
    nutr_662 = db.Column(db.Float)
    nutr_663 = db.Column(db.Float)
    nutr_664 = db.Column(db.Float)
    nutr_665 = db.Column(db.Float)
    nutr_666 = db.Column(db.Float)
    nutr_669 = db.Column(db.Float)
    nutr_670 = db.Column(db.Float)
    nutr_671 = db.Column(db.Float)
    nutr_672 = db.Column(db.Float)
    nutr_673 = db.Column(db.Float)
    nutr_674 = db.Column(db.Float)
    nutr_675 = db.Column(db.Float)
    nutr_676 = db.Column(db.Float)
    nutr_685 = db.Column(db.Float)
    nutr_687 = db.Column(db.Float)
    nutr_689 = db.Column(db.Float)
    nutr_693 = db.Column(db.Float)
    nutr_695 = db.Column(db.Float)
    nutr_696 = db.Column(db.Float)
    nutr_697 = db.Column(db.Float)
    nutr_851 = db.Column(db.Float)
    nutr_852 = db.Column(db.Float)
    nutr_853 = db.Column(db.Float)
    nutr_855 = db.Column(db.Float)
    nutr_856 = db.Column(db.Float)
    nutr_857 = db.Column(db.Float)
    nutr_858 = db.Column(db.Float)
    nutr_859 = db.Column(db.Float)

    weights = db.relationship("Food_weights",backref="food",lazy="dynamic")
    nutrient_data = db.relationship("Food_nutrient_data",backref="food",lazy="dynamic")
    history = db.relationship("FoodHistory",backref="food",lazy="dynamic")

    def __repr__(self):
        return "<Food(ndb_id='%s', long_desc='%s')"%(self.ndb_id,self.long_desc)

class Nutrients(db.Model):
    __tablename__ = 'nut_def'

    nutr_id = db.Column(db.Text, primary_key=True)
    units = db.Column(db.Text)
    tagname = db.Column(db.Text)
    nutr_desc = db.Column(db.Text)
    num_decimal_pts = db.Column(db.Text)
    sr_order = db.Column(db.Text)

    data = db.relationship("Food_nutrient_data",backref="nutrient",lazy="dynamic")
    treatmentdetails = db.relationship("TreatmentDetail",backref="nutrient",lazy="dynamic")

    def __repr__(self):
        return "<Nutrient(nutr_id='%s', nutr_desc='%s')"%(self.nutr_id,self.nutr_desc)

    def __hash__(self):
        return hash((self.nutr_id, self.nutr_desc))

    def __eq__(self, other):
        if type(other)!=type(self):
            return False
        return (self.nutr_id, self.nutr_desc) == (other.nutr_id, other.nutr_desc)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)

class Food_weights(db.Model):

    __tablename__ = 'food_meas'

    index = db.Column(db.BigInteger, primary_key=True)
    ndb_id = db.Column(db.Text,db.ForeignKey('food_desc_full.ndb_id'),index=True)
    seq = db.Column(db.Text)
    amount = db.Column(db.Text)
    measure_desc = db.Column(db.Text)
    gm_weight = db.Column(db.Text)
    num_data_pts = db.Column(db.Text)
    std_dev = db.Column(db.Text)
    history = db.relationship("FoodHistory",backref="weight",lazy="dynamic")

    def __repr__(self):
        return "<Weight(index='%s', measure_desc='%s')"%(self.index,self.measure_desc)


class Food_nutrient_data(db.Model):

    __tablename__ = 'nut_data'

    index = db.Column(db.BigInteger, primary_key=True)
    ndb_id = db.Column(db.Text, db.ForeignKey('food_desc_full.ndb_id'),index=True)
    nutr_id = db.Column(db.Text, db.ForeignKey('nut_def.nutr_id'),index=True)
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

    treatments = db.relationship("Treatments",backref="user",lazy="dynamic")
    symptom_history = db.relationship("SymptomHistory",backref="user",lazy="dynamic")
    
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

class FoodHistory(db.Model):

    __tablename__ = "food_history"
    
    id = db.Column(db.BigInteger, primary_key=True)
    ndb_id = db.Column(db.Text, db.ForeignKey('food_desc_full.ndb_id'),index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),index=True)
    day = db.Column(db.Date)
    meal = db.Column(db.Text) #Breakfast, lunch, dinner, snacks (no validation here yet)
    quantity = db.Column(db.Float) #amount of food eaten
    units = db.Column(db.BigInteger, db.ForeignKey('food_meas.index'),index=True)

    def __init__(self,ndb_id=None,user_id=None,day=None,meal=None,quantity=None,units=None):
        self.ndb_id = ndb_id
        self.user_id = user_id
        self.day=day
        self.meal = meal
        self.quantity = quantity
        self.units = units

class Treatments(db.Model):

    __tablename__ = "treatments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),index=True)
    active = db.Column(db.Boolean)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    details = db.relationship("TreatmentDetail",backref="treatment",lazy="dynamic")

class TreatmentDetail(db.Model):

    __tablename__ = "treatment_details"

    id = db.Column(db.Integer, primary_key=True)
    treatment_id = db.Column(db.Integer, db.ForeignKey('treatments.id'))
    nutr_id = db.Column(db.Text, db.ForeignKey('nut_def.nutr_id'))
    operator = db.Column(db.Text)
    value = db.Column(db.Text) #will be in the units of the nutrient

    def __init__(self,treatment_id = treatment_id,nutr_id = nutr_id, operator=operator,value=value):
        self.treatment_id = treatment_id
        self.nutr_id = nutr_id
        self.operator = operator
        self.value = value

class Symptoms(db.Model):

    __tablename__ = "symptoms"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    history = db.relationship("SymptomHistory",backref="symptom",lazy="dynamic")

    def __init__(self, name=name):
        self.name=name

class SymptomHistory(db.Model):

    __tablename__ = "symptom_history"

    id = db.Column(db.Integer, primary_key=True)
    symptom_id = db.Column(db.Integer, db.ForeignKey('symptoms.id'),index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),index=True)
    value = db.Column(db.Text)
    day = db.Column(db.Date)

    def __init__(self,symptom_id=symptom_id,user_id=user_id,value=value,day=day):
        self.symptom_id = symptom_id
        self.user_id=user_id
        self.value=value
        self.day=day

""" 
# MORE TODO 10/19/18

## we need a way to add custom foods and allow users to specify nutrients

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
"""