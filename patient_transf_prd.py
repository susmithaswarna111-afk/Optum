# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

pat_df = read_bronze_csv("Patient_records")

# COMMAND ----------

#transformation
pat_df = pat_df.fillna({'patient_name':"Visitor/NA"})
pat_df = pat_df.drop('patient_phone')
pat_df = pat_df.withColumn("patient_age", (months_between(current_date(), pat_df.patient_birth_date)/12).cast("integer"))
pat_df = pat_df.drop('patient_birth_date')

# COMMAND ----------

write2silver(pat_df,"Patient_S.csv")