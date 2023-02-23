# Databricks notebook source

from mlops_iris import load_data
from mlops_iris import train
from mlops_iris import predict


# Read the CSV file into a Spark DataFrame
df_spark = spark.read.csv("/dbfs/FileStore/data/01_raw/iris.data", header=True, inferSchema=True)

# Write the Spark DataFrame to Delta format
df_spark.write.format("delta").mode("overwrite").save("/dbfs/FileStore/data/02_raw/")

# Read the Delta table into a Spark DataFrame
df_spark = spark.read.format("delta").load("/dbfs/FileStore/data/02_raw/")

# Convert the Spark DataFrame to a Pandas DataFrame and pass it to the load_split_data function
train_df_pandas, test_df_pandas = load_data.load_split_data(df_spark.toPandas())


