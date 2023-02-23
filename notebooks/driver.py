# Databricks notebook source

from mlops_iris import load_data
from mlops_iris import train
from mlops_iris import predict
import mlflow

experiment_name='/Shared/mlops-iris'
mlflow.set_experiment(experiment_name)

X_train, X_test, y_train, y_test = load_data.load_split_data('/dbfs/FileStore/data/01_raw/iris.data')
model = train.train_model(X_train, X_test, y_train, y_test)
predict.predict(model)
