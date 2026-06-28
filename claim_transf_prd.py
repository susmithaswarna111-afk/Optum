# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

claims_df = read_bronze_json("Claims")

# COMMAND ----------

claims_df = drop_columns(claims_df,['_id'])

# COMMAND ----------

claims.select("*".show())

# COMMAND ----------

claims_df.select("*").filter(col("SUB_ID").isin(["SUBID10022","SUBID10049"])).show(5)

# COMMAND ----------

write2silver(claims_df,"claims_S.csv")
