# import standard libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

# import additional libraries
import pandasql as ps
from pandasql import sqldf

import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols

# functions from .py file
import src.eda_functions as fun

# pysqldf lambda function
pysqldf = lambda q: sqldf(q, globals())

# turn off warnings
import warnings
warnings.simplefilter('ignore', category = DeprecationWarning)
warnings.simplefilter('ignore', category = FutureWarning)

# plot parameters
plt.rcParams['figure.figsize'] = 10, 10
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.titlesize'] = 25
plt.rcParams['xtick.labelsize'] = 18
plt.rcParams['ytick.labelsize'] = 18
plt.rcParams['axes.edgecolor'] = 'black'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['font.size'] = 16



# read in the excel file
df_19 = pd.read_excel('../../data/2019-Report-Card-Public-Data-Set_clean.xlsx', sheet_name="General")


# use clean_col function to standardize column names
fun.clean_col(df_19)

# pysql query to return schools serving grades thru 12
q1 = """SELECT * 
       FROM df_19
       WHERE grades_served LIKE "%12%";"""

hs_19 = pysqldf(q1)

hs_19.percent_student_enrollment_white.replace(np.nan, 0, inplace=True)
hs_19.percent_student_enrollment_black_or_african_american.replace(np.nan, 0, inplace=True)
hs_19.percent_student_enrollment_hispanic_or_latino.replace(np.nan, 0, inplace=True)
hs_19.percent_student_enrollment_asian.replace(np.nan, 0, inplace=True)
hs_19.percent_student_enrollment_native_hawaiian_or_other_pacific_islander.replace(np.nan, 0, inplace=True)
hs_19.percent_student_enrollment_american_indian_or_alaska_native.replace(np.nan, 0, inplace=True)
hs_19.percent_student_enrollment_two_or_more_races.replace(np.nan, 0, inplace=True)
hs_19.number_students_who_took_ap_classes_grade_10_total.replace(np.nan, 0, inplace=True)
hs_19.number_students_who_took_ap_classes_grade_11_total.replace(np.nan, 0, inplace=True)
hs_19.number_students_who_took_ap_classes_grade_12_total.replace(np.nan, 0, inplace=True)


# read in the excel file
df_18 = pd.read_excel('../../data/2018-Report-Card-Public-Data-Set_clean.xlsx', sheet_name="General")


# use clean_col function to standardize column names
fun.clean_col(df_18)

# pysql query to return schools serving grades thru 12
q2 = """SELECT * 
       FROM df_18
       WHERE grades_served LIKE "%12%";"""

hs_18 = pysqldf(q2)

# replace Nan with zero
hs_18.percent_student_enrollment_white.replace(np.nan, 0, inplace=True)
hs_18.percent_student_enrollment_black_or_african_american.replace(np.nan, 0, inplace=True)
hs_18.percent_student_enrollment_hispanic_or_latino.replace(np.nan, 0, inplace=True)
hs_18.percent_student_enrollment_asian.replace(np.nan, 0, inplace=True)
hs_18.percent_student_enrollment_native_hawaiian_or_other_pacific_islander.replace(np.nan, 0, inplace=True)
hs_18.percent_student_enrollment_american_indian_or_alaska_native.replace(np.nan, 0, inplace=True)
hs_18.percent_student_enrollment_two_or_more_races.replace(np.nan, 0, inplace=True)
hs_18.number_students_who_took_ap_classes_grade_10_total.replace(np.nan, 0, inplace=True)
hs_18.number_students_who_took_ap_classes_grade_11_total.replace(np.nan, 0, inplace=True)
hs_18.number_students_who_took_ap_classes_grade_12_total.replace(np.nan, 0, inplace=True)

# read in the excel file
df_17 = pd.read_excel('../../data/2017-Report-Card-Public-Data-Set_clean.xlsx')


# use clean_col function to standardize column names
fun.clean_col(df_17)

# pysql query to return schools servingn grades thru 12
q3 = """SELECT * 
       FROM df_17
       WHERE grades_served LIKE "%12%";"""

hs_17 = pysqldf(q3)

# convert objects to floats
cols_17 = ['high_school_dropout_rate_total',
                 'high_school_4_year_graduation_rate_total',
                 'high_school_5_year_graduation_rate_total',
                 'avg_class_size_high_school',
                 'pupil_teacher_ratio_high_school',
                 'teacher_avg_salary',
                 'teacher_retention_rate',
                 'principal_turnover_within_6_years',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_16_months',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_12_months',
                 'percent_9th_grade_on_track',
                 'number_students_who_took_ap_classes_grade_10_total',
                 'number_students_who_took_ap_classes_grade_11_total',
                 'number_students_who_took_ap_classes_grade_12_total']


hs_17[cols_17] = hs_17[cols_17].apply(pd.to_numeric, errors='coerce', axis=1)


# replacing nans with zeros
hs_17.number_students_who_took_ap_classes_grade_10_total.replace(np.nan, 0, inplace=True)
hs_17.number_students_who_took_ap_classes_grade_11_total.replace(np.nan, 0, inplace=True)
hs_17.number_students_who_took_ap_classes_grade_12_total.replace(np.nan, 0, inplace=True)

# read in the excel file
df_16 = pd.read_excel('../../data/2016-Report-Card-Public-Data-Set_clean.xlsx')

# use clean_col function to standardize column names
fun.clean_col(df_16)

# pysql query to return schools servingn grades thru 12
q4 = """SELECT * 
       FROM df_16
       WHERE grades_served LIKE "%12%";"""

hs_16 = pysqldf(q4)

#convert objects to floats

cols_16 = ['high_school_dropout_rate_total',
                 'high_school_4_year_graduation_rate_total',
                 'high_school_5_year_graduation_rate_total',
                 'avg_class_size_high_school',
                 'pupil_teacher_ratio_high_school',
                 'teacher_avg_salary',
                 'teacher_retention_rate',
                 'principal_turnover_within_6_years',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_16_months',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_12_months',
                 'percent_9th_grade_on_track',
                 'number_students_who_took_ap_classes_grade_10_total',
                 'number_students_who_took_ap_classes_grade_11_total',
                 'number_students_who_took_ap_classes_grade_12_total']


hs_16[cols_16] = hs_16[cols_16].apply(pd.to_numeric, errors='coerce', axis=1)

# replacing nans with zeros
hs_16.number_students_who_took_ap_classes_grade_10_total.replace(np.nan, 0, inplace=True)
hs_16.number_students_who_took_ap_classes_grade_11_total.replace(np.nan, 0, inplace=True)
hs_16.number_students_who_took_ap_classes_grade_12_total.replace(np.nan, 0, inplace=True)

# read in the excel file
df_15 = pd.read_excel('../../data/2015-Report-Card-Public-Data-Set_clean.xlsx')

# use clean_col function to standardize column names
fun.clean_col(df_15)

# use clean_col function to standardize column names
fun.clean_col(df_15)

# pysql query to return schools serving grades thru 12
q5 = """SELECT * 
       FROM df_15
       WHERE grades_served LIKE "%12%";"""

hs_15 = pysqldf(q5)

# convert objects to floats
cols_15 = ['high_school_dropout_rate_total',
                 'high_school_4_year_graduation_rate_total',
                 'high_school_5_year_graduation_rate_total',
                 'avg_class_size_high_school',
                 'pupil_teacher_ratio_high_school',
                 'teacher_avg_salary',
                 'teacher_retention_rate',
                 'principal_turnover_within_6_years',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_16_months',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_12_months',
                 'percent_9th_grade_on_track',
                 'number_students_who_took_ap_classes_grade_10_total',
                 'number_students_who_took_ap_classes_grade_11_total',
                 'number_students_who_took_ap_classes_grade_12_total']


hs_15[cols_15] = hs_15[cols_15].apply(pd.to_numeric, errors='coerce', axis=1)

# read in the excel file
df_14 = pd.read_excel('../../data/2014-Report-Card-Public-Data-Set_clean.xlsx')

# use clean_col function to standardize column names
fun.clean_col(df_14)

# pysql query to return schools serving grades thru 12
q6 = """SELECT * 
       FROM df_14
       WHERE grades_served LIKE "%12%";"""

hs_14 = pysqldf(q6)

# convert objects to floats
cols = ['high_school_dropout_rate_total',
                 'high_school_4_year_graduation_rate_total',
                 'high_school_5_year_graduation_rate_total',
                 'avg_class_size_high_school',
                 'pupil_teacher_ratio_high_school',
                 'teacher_avg_salary',
                 'teacher_retention_rate',
                 'principal_turnover_within_6_years',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_16_months',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_12_months',
                 'percent_9th_grade_on_track',
                 'number_students_who_took_ap_classes_grade_10_total',
                 'number_students_who_took_ap_classes_grade_11_total',
                 'number_students_who_took_ap_classes_grade_12_total']


hs_14[cols] = hs_14[cols].apply(pd.to_numeric, errors='coerce', axis=1)

# read in the excel file
df_13 = pd.read_excel('../../data/2013-Report-Card-Public-Data-Set_clean.xlsx')

# use clean_col function to standardize column names
fun.clean_col(df_13)

# pysql query to return schools serving grades thru 12
q7 = """SELECT * 
       FROM df_13
       WHERE grades_served LIKE "%12%";"""

hs_13 = pysqldf(q7)

# convert objects to floats

cols = ['high_school_dropout_rate_total',
                 'high_school_4_year_graduation_rate_total',
                 'high_school_5_year_graduation_rate_total',
                 'avg_class_size_high_school',
                 'pupil_teacher_ratio_high_school',
                 'teacher_avg_salary',
                 'teacher_retention_rate',
                 'principal_turnover_within_6_years',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_16_months',
                 'percent_graduates_enrolled_in_a_postsecondary_institution_within_12_months',
                 'percent_9th_grade_on_track',
                 'number_students_who_took_ap_classes_grade_10_total',
                 'number_students_who_took_ap_classes_grade_11_total',
                 'number_students_who_took_ap_classes_grade_12_total']


hs_13[cols] = hs_13[cols].apply(pd.to_numeric, errors='coerce', axis=1)

# Concatenate dataframes
final_features=['cohort','rcdts','school_name','district','city','county','district_type', 'district_size',
                'school_type','grades_served','percent_student_enrollment_white',
                'percent_student_enrollment_black_or_african_american',
                'percent_student_enrollment_hispanic_or_latino','percent_student_enrollment_asian',
                'percent_student_enrollment_native_hawaiian_or_other_pacific_islander','percent_student_enrollment_american_indian_or_alaska_native','percent_student_enrollment_two_or_more_races',
                'number_student_enrollment','total_number_of_school_days','student_attendance_rate','student_chronic_truancy_rate',
                'high_school_dropout_rate_total','high_school_4_year_graduation_rate_total','high_school_5_year_graduation_rate_total',
                'avg_class_size_high_school','pupil_teacher_ratio_high_school','teacher_retention_rate',
                'principal_turnover_within_6_years','percent_graduates_enrolled_in_a_postsecondary_institution_within_16_months',
                'percent_graduates_enrolled_in_a_postsecondary_institution_within_12_months','percent_9th_grade_on_track',
                'number_students_who_took_ap_classes_grade_10_total','number_students_who_took_ap_classes_grade_11_total',
                'number_students_who_took_ap_classes_grade_12_total']
final_features
all_dfs=[hs_13, hs_14, hs_15, hs_16, hs_17, hs_18, hs_19]
filtered_dfs=[]

for dataframe in all_dfs:
    filtered_dfs.append(dataframe[final_features])
    
merged_df = pd.concat(all_dfs) 