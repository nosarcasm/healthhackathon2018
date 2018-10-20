# coding: utf-8
from medtracker import app #import init params like where the db is

from flask_sqlalchemy import * #import sql wrapper functions from Flask web helper lib
from sqlalchemy import orm, asc, desc #this is used to give SQLite properties to our Python classes

db = SQLAlchemy(app) #create the db object in sqlalchemy

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
        return "<NutrientData(index='%s', value='%s')"%(self.index,self.nutr_value)