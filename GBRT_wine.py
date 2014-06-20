#Wine Dataset
#Boosted Regression Trees Practice

import pandas as pd
import numpy as np
import pylab as plt
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.grid_search import GridSearchCV



def read_and_combine_dataset():
    url_red = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv'
    url_white = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'

    red = pd.read_csv(url_red, sep = ';')
    white = pd.read_csv(url_white, sep = ';')

    red.head()
    red.describe()

    red['type'] = 0 #red
    white['type'] = 1

    #Combine into one dataset

    wine = red.append(white, ignore_index = True)


    #the DV
    wine['quality'].describe()
    #wine['high_quality'] = wine['quality'] >= 7
    #wine['high_quality'] = wine['high_quality'].astype(int)
    #wine['high_quality']
    return wine

def split_dataset(wine):




    #split the data set
    test_idx = np.random.uniform(0, 1, len(wine)) <= 0.3
    train = wine[test_idx == True]
    test = wine[test_idx == False]
    return(train, test)

def sle(actual, predicted):
    """
    Taken from benhamner's Metrics library.
    Computes the squared log error.
 
    This function computes the squared log error between two numbers,
    or for element between a pair of lists or numpy arrays.
 
    Parameters
    ----------
    actual : int, float, list of numbers, numpy array
             The ground truth value
    predicted : same type as actual
                The predicted value
 
    Returns
    -------
    score : double or list of doubles
            The squared log error between actual and predicted
 
    """
    return (np.power(np.log(np.array(actual)+1) - 
            np.log(np.array(predicted)+1), 2))
 
def rmsle(targets, predictions):
    return np.sqrt((sle(targets, predictions)**2).mean())
    
def train_GBRT(X_train, y_train, X_test, y_test):
    clf = GradientBoostingClassifier(n_estimators = 2500, max_depth = 4, learning_rate = 0.01)
    clf.fit(X_train, y_train)
    return clf

def predict_GBRT(clf):
    clf_pred_1 = clf.predict(X_test)
    return clf_pred_1
    #clf_pred_1 = pd.DataFrame(clf_pred_1, index = bk_test.index, columns = ['count'])
    
def metrics(y_test, clf_pred):
    print 'R^2 Score'
    print r2_score(y_test, clf_pred)
    print 'Mean Squared Error'
    print mean_squared_error(y_test, clf_pred)
    print 'Root Mean Squared Error'
    print np.sqrt(mean_squared_error(y_test, clf_pred))

wine = read_and_combine_dataset()
train, test = split_dataset(wine)

X_vars = wine.columns[:-1]
X_train = train[X_vars]
X_test = test[X_vars]
y_train = train['quality']
y_test = test['quality']

clf = train_GBRT(X_train, y_train, X_test, y_test)
clf_pred_1 = predict_GBRT(clf)
clf_pred_1 = pd.DataFrame(clf_pred_1)
metrics(y_test, clf_pred_1)

plt.figure()
plt.scatter(y_test, clf_pred_1)

#R^2 of 1
#MSE of 0
#RMSE of 0
