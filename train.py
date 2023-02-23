from sklearn.svm import SVC
import pickle
import mlflow
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def train_model(X_train, X_test, y_train, y_test):

    svn = SVC()
    svn.fit(X_train, y_train)

    # Predict from the test dataset
    predictions = svn.predict(X_test)

    # Calculate the accuracy

    accuracy_score(y_test, predictions)

    # A detailed classification report
    print(classification_report(y_test, predictions))

    return svn