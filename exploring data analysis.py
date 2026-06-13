import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")

#1.
print("printing first 5 rows of data",df.head())
print("Dataset info:")
print(df.info())
print("summary statistics")
print(df.describe())

#checking for missing values
print("missing values")
print(df.isnull().sum())

#uniivariate analysis
sns.histplot(df["sepal_length"],kde=True,color="pink")
plt.title("sepal_length")
plt.show()

#bivariate analysis
sns.scatterplot(x="sepal_length",y="petal_length",data=df,hue="species")
plt.title("sepal_length vs petal_length")
plt.show()

#multivariate pair plot
sns.pairplot(df,hue="species")
plt.suptitle("pair_plot",y=1.02)
plt.show()

#correlation heatmap
corr=df.corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("correlation")
plt.show()