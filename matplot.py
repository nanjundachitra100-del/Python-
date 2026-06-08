
#some more with seaborn
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# generate data
x = np.linspace(0, 10, 50)
y = np.sin(x)

plt.plot(x, y, label="sin(x)", color="blue", marker="*")
plt.title("sine wave function", fontsize=10)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

# bar chat
categories=["A","B","C","D"]
VALUES=[10,20,30,40]
plt.bar(categories,VALUES,color="orange")
plt.title("bar chat")
plt.xlabel("categories")
plt.ylabel("Values")
plt.show()

#histogarm
data=np.random.randn(10000)
plt.hist(data,bins=10,color="pink",edgecolor="black")
plt.title("Histogram")
plt.xlabel("student marks")
plt.ylabel("frequency")
plt.show()

#scatter plot
df=sns.load_dataset("tips")
sns.scatterplot(x="total_bill",y="tip",data=df,hue="day")
plt.title("scatter plot")
plt.show()

#box plot
sns.boxplot(x="species",y="petal_length",data=df,palette="set2")
plt.title("box_plot")
plt.show()

#pair plot(seaborn)
sns.pairplot(df,hue="species")
plt.suptitle("pair plot0",y=1.02)
plt.show()

