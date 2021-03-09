import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from sklearn import preprocessing
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.formula.api import ols
from scipy.stats import t
from scipy import stats
from statsmodels.stats.diagnostic import linear_rainbow, het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor



def model(formula_input, data_input):
    x = ols(formula = formula_input, data=data_input)
    y = x.fit()
    return y.summary()


def col_stripper(df, column):
    "Returns column with leading and trailing whitespaces removed."
    return df[column].apply(lambda x: x.strip())



def inspect_panda(obj):
    for x in obj.columns:
        print(x)
        print(obj[x].nunique())
        print('---------')


def lookups(df, lu_type, lu_item=None):
    """
    Return a dataframe from 'df_look' with 'LUType' == lu_type
    and 'LUItem' == lu_item (if specified)
    """
    if lu_item:
        return df[(df.LUType == str(lu_type)) & (df.LUItem == str(lu_item))]
    else:
        return df[(df.LUType == str(lu_type))]
    
column_list = []   
def cleaning_function(obj):
    for x in obj.columns:
        if obj[x].nunique() <= 1:
            column_list.append(x)
    return column_list


def inspect_panda(obj):
    for x in obj.columns:
        print(x)
        print(obj[x].nunique()) #how many unique values does this dataframe contain
        print('---------')



def nans(df):
    return df[df.isnull().any(axis=1)]

def plot_distribution(inp):
    plt.figure()
    ax = sns.distplot(inp)
    plt.axvline(np.mean(inp), color="k", linestyle="dashed", linewidth=5)
    _, max_ = plt.ylim()
    plt.text(
        inp.mean() + inp.mean() / 10,
        max_ - max_ / 10,
        "Mean: {:.2f}".format(inp.mean()),
    )
    return plt.figure

def compare_groups(arr_1, arr_2, alpha, sample_size):
    stat, p = stats.ttest_ind(arr_1, arr_2)
    return 'Statistics=%.3f, p=%.3f' % (stat, p)


