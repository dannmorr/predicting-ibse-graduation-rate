# Prediciting High School Graduation Rate with Machine Learning.
Analysis by Dann Morr

## Repo Structure and Directory
- [Report Notebook](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/notebooks/report/final_report.ipynb)
- [Exploratory Notebooks](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/notebooks/exploratory)
- [Project Presentation](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/reports/presentation.pdf)
- [Data](https://github.com/dannmorr/predicting-ibse-graduation-rate/tree/master/data)
- [src/ directory with project source code](https://github.com/dannmorr/predicting-ibse-graduation-rate/tree/master/src)
- [Figures/ directory with project visuals](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/reports/figures)
- [References](https://github.com/dannmorr/predicting-ibse-graduation-rate/tree/master/references)
- [Project environment](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/environment.yml)



## Table of contents:
- [Project Overview](#Project-Overview)
- [Creating an environment from the environment.yml file](#Creating-an-environment-from-the-environment.yml-file)
- [Data Source](#Data-Source)
- [Data Cleaning](#Data-Cleaning)
- [Exploratory Data Analysis](#Exploratory-Data-Analysis)
- [First Simple Model](#First-Simple-Model)
- [Model Selection](#Model-Selection) 
- [Final Model Evaluation](#Final-Model-Evaluation)
- [Conclusion](#Conclusion)
- [Future Improvement Ideas](#Future-Improvement-Ideas)
- [Presentation Slides](#[Presentation-Slides])
- [Contact Information](#Contact-Information)


## Project Overview

The goal of this project is to create a model that can predict the 4-year graduation rate of a high school cohort based on data regarding the broader structure of the instructional setting and the experience of previous cohorts.

If it is possible to make such a prediction using readily available information it could be possible to spot performance trends, identify cohorts in need of additional resources, or for school to project target goals for improved academic outcomes.

## Creating an environment from the environment.yml file
To run the code in these notebook, use the terminal or an Anaconda Prompt for the following steps:

Create the environment from the [environment.yml](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/environment.yml) file:
`conda env create -f environment.yml`

The first line of the yml file sets the new environment's name. 

Activate the new environment: 
`conda activate myenv`

Verify that the new environment was installed correctly:
`conda env list`


## Data Source
Data was gathered from the Illinois State Board of Education's [Illinois Report Card Data Library](https://www.isbe.net/pages/illinois-state-report-card-data.aspx) website. 
From the website: 
>The Report Card Data Library page is the repository for Report Card data available for public use. Here you can find Statewide Trend Data, Report Card Glossary of Terms, and the public data files from which the Report Card is produced annually.

The data for academic years 2018 and 2019 are each available to download in a single .xlsx Data File.

Gathering the data for each of the academic years 2013 - 2017 involves downloading semi-colon separate .txt Data Files and an accompanying Layout File.

Links for all of the downloads are available in the table below.

Cleaned .xlsx versions of the Data Files are contained in the [data folder](https://github.com/dannmorr/predicting-ibse-graduation-rate/tree/master/data) of this repo. 

Copies of the Layout Files are also available in the [references folder](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/references/Open_Illinois_Report_Card_Data_Files.pdf).

| Year | Link to Data File                                                                                      | Link to Layout File                                                               |
|------|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| 2019 | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/2019-Report-Card-Public-Data-Set.xlsx | n/a                                                                               |
| 2018 | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/Report-Card-Public-Data-Set.xlsx      | n/a                                                                               |
| 2017 | https://www.isbe.net/Documents/rc17.zip                                                                | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/RC17_layout.xlsx |
| 2016 | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/rc16.zip                              | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/RC16-layout.xlsx |
| 2015 | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/rc15.zip                              | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/RC15-layout.xlsx |
| 2014 | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/rc14.zip                              | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/RC14_layout.xlsx |
| 2013 | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/2013-rc-separated.zip                 | https://www.isbe.net/_layouts/Download.aspx?SourceUrl=/Documents/RC13_layout.xlsx |

Instructions for Opening the Report Card Data Files is available in the [references folder](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/references/Open_Illinois_Report_Card_Data_Files.pdf) or can be downloaded [here](https://www.isbe.net/Documents/Open_Illinois_Report_Card_Data_Files.pdf).

>"The Illinois Report Card data files that are available for download from ISBE’s website do not include a header row. You must refer to the companion report card file layout Excel document to understandhow the data is organized within the worksheet."

While performing the tasks of downloading the files, and reviewing the contents and Layout Files, I also began to narrow down my selected feature set to use for this project. From the Data Files, I identified 35 features across these 6 categories that I felt would give an adequate holistic view on the students' experience:

**1. General School Information**
 - school_name
 - district
 - city
 - county
 - district_type
 - district_size
 - school_type
 - grades_served
 
**2. Student Demographics**
 - percent_student_enrollment_white
 - percent_student_enrollment_black_or_african_american
 - percent_student_enrollment_hispanic_or_latino
 - percent_student_enrollment_asian
 - percent_student_enrollment_native_hawaiian_or_other_pacific_islander
 - percent_student_enrollment_american_indian_or_alaska_native
 - percent_student_enrollment_two_or_more_races
 - number_student_enrollment
 - total_number_of_school_days
 - student_attendance_rate
 - student_chronic_truancy_rate
 - high_school_dropout_rate_total
 - high_school_4_year_graduation_rate_total
 - high_school_5_year_graduation_rate_total
 
**3. Instructional Setting**
 - avg_class_size_high_school
 
**4. Teacher and Administrator Statistics**
 - pupil_teacher_ratio_high_school
 - teacher_avg_salary
 - teacher_retention_rate
 - principal_turnover_within_6_years
 
**5. College and Career Readiness**
 - percent_graduates_enrolled_in_a_postsecondary_institution_within_16_months
 - percent_graduates_enrolled_in_a_postsecondary_institution_within_12_months
 - percent_9th_grade_on_track
 
**6. Advanced Coursework**
 - number_students_who_took_ap_classes_grade_10_total
 - number_students_who_took_ap_classes_grade_11_total
 - number_students_who_took_ap_classes_grade_12_total

### Inspecting the Data

 Each row in the data sets represents one school in a given academic year. These data sets include all public and charter schools in Illinois serving grades PreK - 12.

The number of columns varied greatly from set to set (from 800 on the low end to 9,000 on the high end), as did the parameters that were recorded from one year to the next. The features listed above were consistenly available throughout these data files.

I will use the following cohorts for training the data:

- 2017
- 2016
- 2015
- 2014
- 2013

My validation set will be: 
- 2018

My test set will be 
- 2019

The target variable is **4-year high school graduation rate**.

### Data Cleaning

This is a brief overview of the steps taken to clean the data and combine the files into one working DataFrame.
The details can be seen in [notebooks/exploratory/01_cleaning_and_compiling](https://github.com/dannmorr/predicting-ibse-graduation-rate/blob/master/notebooks/exploratory/01_cleaning_and_compiling.ipynb)

1. Read in each cohort data file and create a dataframe for schools that serve grades 9 - 12.

    I chose this parameter because there are some charter schools, and schools in smaller districts that serve more grades than 9-12 (and a couple that serve 10-12 or just 11-12. 

    If they serve through grade 12, they submit graduation rate information. If they do not serve grade 12, they do not contain my target variable.
    
2. Convert numeric columns from 'object' to 'float'. Many of the columns had numeric values that were recorded as strings. These were converted to numbers. In some cases this revealed missing values that were replaced with zeros (see next step), others were later imputed with mean values - after performing a train test split. 

3. Fill in NaNs with zeros as appropriate:
    For example, looking at percentages of student demographics, all groups may not be represented and, therefore, cells left blank instead of recording a zero.
    Similarly, not all schools offer Advanced Placement classes for grades 10, 11 and 12. Where these are blank, they have been recorded as zeros.
    
4. Several columns were dropped due to missing values that could not be corrected by zeros or mean values.

## Exploratory Data Analysis 

Looking at the correlation to the target variable of 4-year graduation rates

![heatmap](./reports/figures/heatmap.png)

This heatmap shows the postive and negative correlations to the target variable.

Not surprisingly, features such as 5-year graduation rate, student attendance rate, and teacher retention rate have a strong positive correlation to 4-year graduation. While high school dropout rate and chronic truancy have a strong negative correlation.

**A note about 4-year vs 5-year graduation**: A student who completes all graduation requirements in the traditional 4-year schedule is included in the 4-year graduation rate total. If a student takes an extra year to complete all graduation requirements they are included in the 5-year graduation rate total. They may graduate in the same year, but are counted separately in the data. 

## First Simple Model

This model returned an R-squared value of 0.445, indicating that less than 50% of the the variance in the target variable is predictable from the features. This was the baseline model, did not include any of the categorical features, and there was no feature engineering or hyperparameter tuning. That leaves me feeling optimistic that I can improve on this with all of the above.

## Model selection
For model selection, I decided to compare several models on their default settings and the same random state (19).

The models I chose are 
- Linear Regression
- Random Forest Regressor
- Extra Trees Regressor
- Lasso
- Ridge
- Gradient Boosting Regressor
- Support Vector Regressor
- K-Nearest Neighbor Regressor

The results are plotted below.

![model_compare.png](./reports/figures/model_compare.png)

Gradient Boosting returned the highest R-squared value: 0.557.

I then employed RandomizedSearchCV to determine the optimal settings for the hyperparameters.
#### The model returned an R-squared value of 0.589.

## Final Model Evaluation

#### The final model returned an R-squared value of 0.684.
That is a surprisingly good result on the test data. The R-squared values have been steadily increasing throughout is process, as seen in the chart below:

| Model                                         | Evaluated on   | R-Squared Score |
|-----------------------------------------------|----------------|-----------------|
| Ordinary Least Squares  Linear Regression     | Validation set | 0.445           |
| Gradient Boosting Regressor (default setting)   | Validation set | 0.557           |
| Gradient Boosting Regressor (optimized setting) | Validation set | 0.589           |
| Gradient Boosting Regressor (optimized setting) | Test set       | 0.684           |

From the First Simple Model to the Final Model there was an increase of approximately 24 percentage points.
This indicates that the model is improving at each iteration.
Although the R-squared values are increasing, there are no giant leaps that suggest overfitting.

## Conclusion

At this point, I feel this result is a "proof of concept" for the project. The R-squared value of 0.684 on the final model does not satisfy me that it could be used for predictions in the real world at this time. However, there is still the possibility of building upon this start and attempting to improve its' ability.

## Future Improvement Ideas

Some ideas I would like to pursue include:
- optimizing some of the other models I tried during selection.
Gradient Boosting returned the highest value in the default state, but Ridge, KNN, Lasso, and Extra Trees were all close behind.

- additional feature engineering and feature selection
I would like to reassess some of the features that I eliminated in EDA.
Perhaps it would be possible to find more about the missing values, include some of the data recorded at the district level, and possibly look at including financial, tax, or census information.

- new code for data cleaning
As a side note to the model building: If I join more data sources, I would like to work on some code to gather and compile data more elegantly and efficiently.

## Contact

#### Dann Morr [GitHub](https://github.com/dannmorr) | [LinkedIn](https://linkedin.com/in/dannmorr) | [Medium](https://medium.com/@dannmorr) | [Email](mailto:dannmorr@gmail.com)
