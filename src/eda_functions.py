import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import statsmodels.formula.api as smf
from sklearn.metrics import r2_score



def clean_col(df):

    '''
    Clean columns headers in df
    '''
    df.columns = [x.lower()
                 .replace("-", " ")
                 .replace("  ", " ")
                 .replace(" ", "_")
                 .replace("__", "_")
                 .rstrip()
                 .replace("#", "number")
                 .replace("%", "percent") for x in df.columns]
    
def to_obj(df, col):
    ''' 
    Change column from 'int' to 'object'
    '''
    df[col] = df[col].astype('object')    




def proj_eda(df): 
        
    '''
    ***************************************************************************************/
    *    Title: GraphicsDrawer source code
    *    Author: Smith, J
    *    Date: 2011
    *    Code version: 2.0
    *    Availability: http://www.graphicsdrawer.com
    *
    ***************************************************************************************/
    EDA functions
    
    '''
    eda_df = {}
    eda_df['null_sum'] = df.isnull().sum()
    eda_df['null_pct'] = df.isnull().mean()
    eda_df['dtypes'] = df.dtypes
    eda_df['count'] = df.count()
    eda_df['mean'] = df.mean()
    eda_df['median'] = df.median()
    eda_df['min'] = df.min()
    eda_df['max'] = df.max()
    
    return pd.DataFrame(eda_df)





def heatmap(df, dependent_variable):
    '''
    ***************************************************************************************/
    *    Title: Creating Python Functions for Exploratory Data Analysis and Data Cleaning
    *    Author: Xin, F
    *    Date: 2020
    *    Availability: https://github.com/FredaXin/blog_posts/blob/master/creating_functions_for_EDA.md
    *
    ***************************************************************************************/
    Takes df, a dependant variable as str
    Returns a heatmap of all independent variables' correlations with dependent variable 
    '''

    plt.figure(figsize=(8, 8))
    g = sns.heatmap(df.corr()[[dependent_variable]].sort_values(by=dependent_variable), 
                    annot=True, 
                    cmap='YlGnBu', 
                    cbar=False,
                    vmin=-1,
                    vmax=1)  
    return g




def forward_selected(data, response):
    """Linear model designed by forward selection.
    ***************************************************************************************/
    *    Title: Forward Selection with statsmodels
    *    Author: Schumacher, A and Smith, T
    *    Date: 2015
    *    Availability: https://planspace.org/20150423-forward_selection_with_statsmodels/
    *
    ***************************************************************************************/

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response

    response: string, name of response column in data

    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by adjusted R-squared
    """
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(response,
                                   ' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return model


# instantiates, fits, and trains a model.
# returns adjusted r2_score
def fit_and_eval(model, X_t, y, X_v):
    #X_t = X_train_all
    #X_v = X_val_all
    #y = y_train
    # Train the model
    model.fit(X_t, y)
    
    # Make predictions and evalute
    model_pred = model.predict(X_v)
    model_r2 = r2_score(y_val, model_pred)
    adj_r2 = round((1-(1-model_r2))*((3403-1)/(3403-23-1)), 3)

    # Return the performance metric
    return print(f'Adjusted R-squared on Validation Set: {adj_r2}')