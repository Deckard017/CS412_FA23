import random
import numpy as np
from xgboost import XGBClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def get_splits(n, k, seed):
  splits=None
  # Implement your code to construct the splits here
  np.random.seed(seed)
  out_lists=list(range(n))
  np.random.shuffle(out_lists)
  splits=[]
  left_most=0
  for i in range(k):
    size=n//k
    if i<n%k:
      size+=1
    split_one=out_lists[left_most:left_most+size]
    splits.append(split_one)
    left_most+=size
  return splits

def my_cross_val(method, X, y, splits):
  errors=[]
  # train_indices=[]
  for split in splits:
    train_indices=[i for i in range(len(X)) if i not in split]
    # train_indices.extend(train_indice)
    test_indices=split
    train_indices.sort()
    test_indices.sort()
    if method=='LinearSVC':
      classifier=LinearSVC(max_iter=2000,random_state=412)
    elif method=='SVC':
      classifier=SVC(gamma='scale',C=10,random_state=412)
    elif method=='LogisticRegression':
      classifier=LogisticRegression(penalty='l2',solver='lbfgs',random_state=412,multi_class='multinomial')
    elif method=='RandomForestClassifier':
      classifier=RandomForestClassifier(max_depth=20,n_estimators=500,random_state=412)
    elif method=='XGBClassifier':
      classifier=XGBClassifier(max_depth=5,random_state=412)
  # Implement your code to calculate the errors here
    X_training=X[train_indices]
    y_training=y[train_indices]
    X_test=X[test_indices]
    y_test=y[test_indices]

    classifier.fit(X_training,y_training)
    y_prediction=classifier.predict(X_test)
    error_predictions=(y_prediction!=y_test).sum()
    error_rate=error_predictions/len(y_test)
    errors.append(error_rate)
  return np.array(errors)