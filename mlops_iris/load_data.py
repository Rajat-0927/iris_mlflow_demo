import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def load_split_data(file_path):
    columns = ['Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Class_labels'] # As per the iris dataset information

    # df_test=pd.read_csv(file_path)
    # print(df_test)
                        
    # Load the data
    # df = pd.read_csv(file_path, names=columns)
    df = file_path

    df.head()

    # Seperate features and target  
    data = df.values
    X = data[:,0:4]
    Y = data[:,4]

    # Split the data to train and test dataset.
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
    
    return X_train, X_test, y_train, y_test