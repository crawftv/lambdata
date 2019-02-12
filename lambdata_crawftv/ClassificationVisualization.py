#!/usr/bin/env python

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
def classification_visualization(y_true,y_pred):
    print(generate_visualization(y_true,y_pred)[0])
    print(generate_visualization(y_true,y_pred)[1])
                
def generate_visualization(y_true,y_pred):
    return confusion_viz(y_true,y_pred),classification_report(y_true,y_pred)
def confusion_viz(y_true, y_pred):
    matrix = confusion_matrix(y_true,y_pred)
    return sns.heatmap(matrix, annot=True,
        fmt=',', linewidths=1,linecolor='grey',
        square=True,
        xticklabels=['Predicted\nNO', 'Predicted\nYES'], 
        yticklabels=['Actual\nNO', 'Actual\nYES'])
