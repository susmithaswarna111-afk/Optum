# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

hos_df = read_bronze_csv("Hospital")

# COMMAND ----------

#transformation
hos_df = hos_df.replace("NaN",None)
hos_df = hos_df.fillna({'state':"UT"})
hos_df = hos_df.replace("New Delhi", "Delhi")

# COMMAND ----------

write2silver(hos_df,"Hospital_S.csv")