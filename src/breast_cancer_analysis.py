# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZNX5rNdQhWiI0LWJol2dtYUQhZPdstbs

# Demo notebook for BIMM05
## This notebook will focus on how to work with CSV files
"""

import pandas as pd
import seaborn as sns
from scipy.stats import mannwhitneyu

"""### Importing data"""

data_link = 'https://raw.githubusercontent.com/parashardhapola/bimm05/6e089fd63a42b799caceaf4fed6dc858ad7671db/data/external/breast_cancer_wisonsin.csv'

df = pd.read_csv(data_link)

"""### Inspecting dataframe"""

df.shape

df.head()

df.columns

df['diagnosis'].value_counts()

df['radius_mean'].mean()

df['radius_mean'].min(), df['radius_mean'].max()

"""### Visualizing data"""

sns.histplot(data=df, x='radius_mean', hue='diagnosis')

sns.violinplot(data=df, y='radius_mean', x='diagnosis')

"""### Grouping data"""

df.groupby('diagnosis')['radius_mean'].mean()

"""### Performing statistical tests"""

idx = df['diagnosis'] == 'B'
b_radius = df['radius_mean'][idx]

idx = df['diagnosis'] == 'M'
m_radius = df['radius_mean'][idx]

b_radius

m_radius

mannwhitneyu(b_radius, m_radius)

