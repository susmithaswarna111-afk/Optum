# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

dis_df = read_bronze_csv("disease")

# COMMAND ----------

df_row_columns(dis_df)

# COMMAND ----------

check_missing_values(dis_df,dis_df.columns)

# COMMAND ----------

check_string_as_nan(dis_df)

# COMMAND ----------

check_duplicates(dis_df,dis_df.columns)

# COMMAND ----------

display(dis_df)  #action

# COMMAND ----------

display(dis_df)

# COMMAND ----------

write2silver(dis_df,"Diease_S.csv")