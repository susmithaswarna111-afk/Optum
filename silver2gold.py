# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

list_silver_files()

# COMMAND ----------

grp = read_silver_csv("Group_S")
subgrp = read_silver_csv("SubGroup_S")
clams = read_silver_csv("claims_S")
dise = read_silver_csv("disease_S")
hos = read_silver_csv("Hospital_S")
pat = read_silver_csv("Patient_S")
sub = read_silver_csv("Subscriber_S")

# COMMAND ----------

display(grp.limit(5))

# COMMAND ----------

display(subgrp.limit(5))

# COMMAND ----------

#1st join
grp_subgrp_df = grp.join(subgrp, grp.grp_id == subgrp.subgrp_id, "inner")

# COMMAND ----------

display(grp_subgrp_df.limit(5))

# COMMAND ----------

display(hos.limit(5))

# COMMAND ----------

display(pat.limit(5))

# COMMAND ----------

#2nd join
pat_hos_df = hos.join(pat, hos.Hospital_id == pat.hospital_id, "inner")

# COMMAND ----------

display(pat_hos_df.limit(10))

# COMMAND ----------

#3rd join
pat_hos_claims_df = pat_hos_df.join(clams, pat_hos_df.Patient_id == clams.patient_id, "inner")

#4th join)

optum_df = pat_hos_claims_df.join(sub, pat_hos_claims_df['sub_id'] == sub.sub_id, "inner")

# COMMAND ----------

display(optum_df)

# COMMAND ----------

write2gold(optum_df,"Optum_G.csv")
write2sqldatabase(optum_df,"Optum_G_Tb")