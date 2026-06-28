# Databricks notebook source
def sample_data(df):
    display(df.limit(5))
    return "Sample Data"

# COMMAND ----------

def install_libraries():
    from pyspark.sql.functions import col, lit, sum
    from pyspark.sql import DataFrameWriter
    print("required libraries imported sucessfully")

# COMMAND ----------

install_libraries()

# COMMAND ----------

def list_bronze_files():
    display(dbutils.fs.ls("/mnt/optumbrzpt/"))
    return "Bronze files List"

# COMMAND ----------

def list_silver_files():
    display(dbutils.fs.ls("/mnt/optumslvpt/"))
    return "Silver files List"

# COMMAND ----------

def list_gold_files():
    display(dbutils.fs.ls("/mnt/optumgldpt/"))
    return "Gold files List"

# COMMAND ----------

def read_bronze_csv(df):
    data = spark.read.csv("/mnt/optumbrzpt/"+df+".csv", header=True, inferSchema=True)
    print("Data Read Sucessfully")
    return data

# COMMAND ----------

def read_bronze_json(df):
    data = spark.read.json("/mnt/optumbrzpt/"+df+".json")
    print("Data Read Sucessfully")
    return data

# COMMAND ----------

def read_silver_csv(df):
    data = spark.read.csv("/mnt/optumslvpt/"+df+".csv", header=True, inferSchema=True)
    print("Data Read Sucessfully")
    return data

# COMMAND ----------

def read_gold_csv(df):
    data = spark.read.csv("/mnt/optumgldpt/"+df+".csv", header=True, inferSchema=True)
    print("Data Read Sucessfully")
    return data

# COMMAND ----------

from pyspark.sql import DataFrameWriter

# COMMAND ----------

def write2sqldatabase(df,table_name):
    server = dbutils.secrets.get(scope="optumscope", key="azuresqlserver")
    port = "1433"
    database = "optum_db"
    db_properties = {"user": dbutils.secrets.get(scope="optumscope", key="azuresqlseruser") ,"password": dbutils.secrets.get(scope="optumscope", key="azuresqlserpass")}
    serverurl = "jdbc:sqlserver://{0}:{1};database={2}".format(server, port, database)
    output = DataFrameWriter(df)
    output.jdbc(url = serverurl, table = table_name, mode = "overwrite", properties = db_properties)
    print("*****Successfully written in Database*******")

# COMMAND ----------

def write2silver(df,file_name):
    silver_path = "/mnt/optumslvpt/"
    temp_path = f"{silver_path}/output_temp"
    final_path = f"{silver_path}/{file_name}" 
    df.write.mode("overwrite").option("header","true").csv(temp_path)
    files = dbutils.fs.ls(temp_path)
    csv_file = [file.path for file in files if file.path.endswith(".csv")][0]
    dbutils.fs.mv(csv_file,final_path)
    dbutils.fs.rm(temp_path,recurse=True)
    print('File written to silver')

# COMMAND ----------

def write2gold(df,file_name):
    gold_path = "/mnt/optumgldpt/"
    temp_path = f"{gold_path}/output_temp"
    final_path = f"{gold_path}/{file_name}" 
    df.write.mode("overwrite").option("header","true").csv(temp_path)
    files = dbutils.fs.ls(temp_path)
    csv_file = [file.path for file in files if file.path.endswith(".csv")][0]
    dbutils.fs.mv(csv_file,final_path)
    dbutils.fs.rm(temp_path,recurse=True)
    print('File written to gold')