# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

grp_df = read_bronze_csv("group")

# COMMAND ----------

write2silver(grp_df,"Group_S.csv")