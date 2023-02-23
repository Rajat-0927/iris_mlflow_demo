import numpy as np

def predict(model):
    X_new = np.array([[3, 2, 1, 0.2], [  4.9, 2.2, 3.8, 1.1 ], [  5.3, 2.5, 4.6, 1.9 ]])
    prediction=model.predict(X_new)
    print("Prediction of Species: {}".format(prediction))