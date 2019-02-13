import sklearn
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np
import pandas as pd

"""classification_visualization is the key function
   classification_report is just the sklearn classification report
   classificaiton_report will show up in the shell
"""
def classification_visualization(y_true,y_pred):
    print(classification_report(y_true,y_pred))
    print(confusion_viz(y_true,y_pred))
"""confusion_viz is inspired from code from a Ryan Herr Lambda School Lecture
   confusion_viz shows up in a notebook.
"""
def confusion_viz(y_true, y_pred):
    y_true = np.array(y_true)
    y_true = pd.Series(y_true.ravel())
    labels = y_true.value_counts().index
    matrix = confusion_matrix(y_true, y_pred)
    return sns.heatmap(matrix, annot=True,
                       fmt=',', linewidths=1,linecolor='grey',
                       square=True,
                       xticklabels=["Predicted\n" + str(i) for i in labels],
                       yticklabels=["Actual\n" + str(i) for i in labels],
                       robust=True,
                       cmap=sns.color_palette("coolwarm"))
