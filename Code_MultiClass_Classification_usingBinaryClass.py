## problem of multiclass/multilabel classification is broken down to multiple binary classification problem using OneVsRestClassifier
##used Linear Support Vector Classification fir binary
 import numpy as np
 from sklearn.multiclass import OneVsRestClassifier
 from sklearn.svm import SVC
 X = np.array([
        [10, 10],
        [8, 10],
        [-5, 5.5],
        [-5.4, 5.5],
        [-20, -20],
        [-15, -20]
    ])
 y = np.array([0, 0, 1, 1, 2, 2])
 clf = OneVsRestClassifier(SVC()).fit(X, y)
 clf.predict([[-19, -20], [9, 9], [-5, 5]])  ### multi class prediction
 