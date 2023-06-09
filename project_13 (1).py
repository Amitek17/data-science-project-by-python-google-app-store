# -*- coding: utf-8 -*-
"""Project 13

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DnTnCROxbHghkCjoKJviwcwKvgklKBS0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sc

data=pd.read_csv('/content/Google Apps data.csv')

data

# checking nan values.....
data.isnull().sum()

# missing value percentage....
(data.isnull().sum()/data.shape[0])*100

# hist plot for rating.......
xt=data['Rating'].hist(bins=15, density=True, stacked=True, color='teal', alpha=0.6)
data["Rating"].plot(kind='density', color='teal')

plt.grid()
plt.xlim(-10.5,10.5)
plt.show()

# cleaning of rating data
t_data=data[pd.notnull(data['Rating'])]

# mean,median,mode
mean=np.mean(t_data['Rating'])
median=np.median(t_data['Rating'])
mode=sc.mode(t_data['Rating'])

print(mean,median,mode)

# rating is right skewed so take median in place of nan
data['Rating'].fillna(median,inplace=True)

# In other features missing value % is not considrable so drop nan
data.dropna(inplace=True)

data.info()

# Remove dublicate values

(data.duplicated().value_counts()/data.shape[0])*100

data.drop_duplicates(inplace=True)

data.info()

"""Data preprocessing"""

# converting last date
data['Last Updated']=pd.to_datetime(data['Last Updated'])
data['before update']=data['Last Updated'].max()-data['Last Updated']

# converting review to int
data['Reviews']=data['Reviews'].astype('int')

data.describe()

"""Data visualisation"""

# most Most popular category
plt.figure(figsize=(40,10))
data['Category'].value_counts().plot(kind='pie')
plt.show()
plt.figure(figsize=(40,10))
data['Category'].value_counts().plot(kind='bar')
plt.xlabel('Category')
plt.ylabel('freq.')
plt.grid()
plt.show()

#  Content Rating 


plt.figure(figsize=(5,5))
data['Content Rating'].value_counts().plot(kind='bar')
plt.xlabel('Content Rating')
plt.ylabel('freq.')

plt.grid()
plt.show()

data['Size'].value_counts()

plt.figure(figsize=(40,10))
data['Genres'].value_counts().plot(kind='bar')
plt.xlabel('Genres')
plt.ylabel('freq.')
plt.show()

plt.figure(figsize=(10,10))
explode=[0.1,0]
data['Type'].value_counts().plot(kind='pie',autopct="%2i%%",explode=explode)
plt.legend()
plt.show()
plt.figure(figsize=(10,10))
data['Type'].value_counts().plot(kind='bar')
plt.xlabel('Type')
plt.ylabel('freq.')
plt.show()

# max size app
data[data['Size']==data['Size'].max()]

# max size install app
data[data['Installs']==data['Installs'].max()]

# App which hasn't been updated
data[data['before update']==data['before update'].max()]

# App with largest number of reviews
data[data['Reviews']==data['Reviews'].max()]

##B most reviewed apps
import seaborn as sns
sorte = data.sort_values(['Reviews'],ascending = 0 )[:20]
ax = sns.barplot(x = 'Reviews' , y = 'App' , data = sorte )
ax.set_xlabel('Reviews')
ax.set_ylabel('')
ax.set_title("Most Popular Categories in App Store", size = 20)