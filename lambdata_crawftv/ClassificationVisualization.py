import sklearn
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""IMPORTANT must upgrade Seaborn to use in google Colab.
"""
"""classification_visualization is the key function
   classification_report is just the sklearn classification report
   classification_report will show up in the shell
"""
def classification_visualization(y_true,y_pred):
    print(classification_report(y_true,y_pred))
    print(confusion_viz(y_true,y_pred))
"""confusion_viz is inspired from code from a Ryan Herr Lambda School Lecture
   confusion_viz shows up in a notebook.
   no custom labeling yet. uses labels as given.
   pass y_true,y_pred, same as any sklearn classification problem
"""
def confusion_viz(y_true, y_pred):
    y_true = np.array(y_true)
    y_true = pd.Series(y_true.ravel())
    labels = unique_labels(y_true,y_pred)
    matrix = confusion_matrix(y_true, y_pred)
    graph = sns.heatmap(matrix, annot=True,
                       fmt=',', linewidths=1,linecolor='grey',
                       square=True,
                       xticklabels=["Predicted\n" + str(i) for i in labels],
                       yticklabels=["Actual\n" + str(i) for i in labels],
                       robust=True,
                       cmap=sns.color_palette("coolwarm"))
    plt.yticks(rotation=0)
    plt.xticks(rotation=0)
    return graph
