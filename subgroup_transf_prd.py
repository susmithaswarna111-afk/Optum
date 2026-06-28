# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

subgrp_df = read_bronze_csv("subgroup")

# COMMAND ----------

#transformation
subgrp_df = subgrp_df.withColumn("subgrp_id", split(col("subgrp_id"),","))
subgrp_df = subgrp_df.withColumn("subgrp_id", explode(col("subgrp_id")))

# COMMAND ----------

write2silver(subgrp_df,"SubGroup_S.csv")