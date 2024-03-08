"""
    This short script loads all labels, color schemes, marker styles, and line styles.
    The order of property list follows the Supplementary Table S13 of Supporting Information in Y. Liu et al.
"""
from copy import deepcopy
import pandas as pds
import numpy as np

model_label_csv = pds.read_csv('labels/MLPmodel.csv')

category_tmp_csv = pds.read_csv('labels/Categories.csv')
cdict = {}
for v in category_tmp_csv.keys():
    cdict[v] = []
for ik, k in enumerate(category_tmp_csv['content']):
    for v in category_tmp_csv.keys():
        if v!='content':
            cdict[v].append(category_tmp_csv[v][ik])
        else:
            cdict[v].append(deepcopy(k.split(', ')))
category_label_csv = pds.DataFrame(cdict)

property_label_csv = pds.read_csv('labels/Properties.csv')
train_label_csv = pds.read_csv('labels/TrainingData.csv')