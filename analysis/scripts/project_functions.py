import pandas as pd
import numpy as np
import seaborn as sns


def load_and_process():

    # Chain 1: import the data and remove unwanted columns
    df1 = (
        pd.read_csv("../data/raw/allCetaceanData.csv")
        .drop('mother',axis='columns')
        .drop('father',axis='columns')
        .drop('region',axis='columns')
        .drop('transfer',axis='columns')
        .drop('transferDate',axis='columns')
        .drop('notes', axis = 'columns')
    )
    
    # Chain 2: change columns to datetime, remove timestamps, create timespent calculated column
    df2 = df1.assign(
        originDate=lambda x: pd.to_datetime(x['originDate']).dt.date,
        statusDate=lambda x: pd.to_datetime(x['statusDate']).dt.date,
        timespent=lambda x: x['statusDate'] - x['originDate']
    )
    
    # Chain 3: change birthdate accuracy value labels
 
    df3 = (
        df2.replace('a','actual')
        .replace('e','estimate')
        .replace('u','unknown')
    )
    
    return df3