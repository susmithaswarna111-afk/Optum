# Databricks notebook source
def df_row_columns(df):
  return df.count(), len(df.columns)

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

def check_missing_values(df, lst_cl):    #lst_cl = ['id', 'member_id', 'loan_amnt']
    missing_values = {}
    for i in lst_cl:
        a = df.filter(col(i).isNull()).count() 
        missing_values[i] = a
    return missing_values

# COMMAND ----------

def check_missing_values_percent_v1(df, lst_cl):
    global missing_values_percent_less_than_75
    global missing_values_percent_more_than_75
    missing_values_percent_less_than_75 = {}
    missing_values_percent_more_than_75 = {}
    b = df.count()
    for i in lst_cl:
        a = df.filter(col(i).isNull()).count() 
        c = (a/b) * 100
        if c >= 75:
            missing_values_percent_more_than_75[i] = c
        else:
            missing_values_percent_less_than_75[i] = c
    return ({"missing_values_percent_more_than_75: ":missing_values_percent_more_than_75,   \
            "missing_values_percent_less_than_75: ":missing_values_percent_less_than_75})

# COMMAND ----------

def drop_columns(df, col_lst):
    for i in col_lst:
        df = df.drop(i)
        print("Columns Dropped: ",i)
    return df

# COMMAND ----------

def check_duplicates(df,cl):
    a = df.select(cl).distinct().count()
    b = df.count()
    if a == b:
        print("No Duplicates")
    else:
        c = b - a
        print("There are ",c,"Duplicates")

# COMMAND ----------

def display_data(df):
    return display(df.limit(20))

# COMMAND ----------

def check_string_as_nan(df):
    result = {}
    for i in df.columns:
        result[i] = df.filter(col(i).like("%NaN%")).count()
    print(result)


# COMMAND ----------

