# coding: utf-8
from sqlalchemy import Column, MetaData, Table, Text

metadata = MetaData()


t_food_desc = Table(
    'food_desc', metadata,
    Column('NDB_No', Text, index=True),
    Column('FdGrp_Cd', Text),
    Column('Long_Desc', Text),
    Column('Shrt_Desc', Text),
    Column('ComName', Text),
    Column('ManufacName', Text),
    Column('Survey', Text),
    Column('Ref_desc', Text),
    Column('Refuse', Text),
    Column('SciName', Text),
    Column('N_Factor', Text),
    Column('Pro_Factor', Text),
    Column('Fat_Factor', Text),
    Column('CHO_Factor', Text)
)


t_food_meas = Table(
    'food_meas', metadata,
    Column('NDB_No', Text, index=True),
    Column('Seq', Text),
    Column('Amount', Text),
    Column('Msre_Desc', Text),
    Column('Gm_Wgt', Text),
    Column('Num_Data_Pts', Text),
    Column('Std_Dev', Text)
)


t_nut_data = Table(
    'nut_data', metadata,
    Column('NDB_No', Text, index=True),
    Column('Nutr_No', Text),
    Column('Nutr_Val', Text),
    Column('Num_Data_Pts', Text),
    Column('Std_Error', Text),
    Column('Src_Cd', Text),
    Column('Deriv_Cd', Text),
    Column('Ref_NDB_No', Text),
    Column('Add_Nutr_Mark', Text),
    Column('Num_Studies', Text),
    Column('Min', Text),
    Column('Max', Text),
    Column('DF', Text),
    Column('Low_EB', Text),
    Column('Up_EB', Text),
    Column('Stat_Cmt', Text),
    Column('AddMod_Date', Text)
)


t_nut_def = Table(
    'nut_def', metadata,
    Column('Nutr_No', Text, index=True),
    Column('Units', Text),
    Column('Tagname', Text),
    Column('NutrDesc', Text),
    Column('Num_Dec', Text),
    Column('SR_Order', Text)
)
