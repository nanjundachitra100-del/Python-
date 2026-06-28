import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("iris")

#basic inspction
print("first 5 rows of dataset:",df.head())
print("data information")
print(df.info())
print("summary statistics")
print(df.describe)

#check missing values
print("missing values")
print(df.isnull().sum())

#univariate variables
sns.histplot(df['sepal_length'],kde=True,color="orange",bins=20)
plt.title("histogram")
plt.show()

#bivariate
sns.scatterplot(x="sepal_length",y="petal_length",hue="species",data=df)
plt.title("scatter plot")
plt.show()

#multivariate
sns.pairplot(df,hue="species")
plt.suptitle("pairplot format",y=1.2)
plt.show()

#correlation
corr=df.select_dtypes(include=['number']).corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("correlation heatmap")
plt.show()


