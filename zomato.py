import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("zomato-data.csv")
print(df.head)
print(df)

def convertRate(rate):
    val = str(rate).split("/")
    return float(val[0])

df['rate'] = df['rate'].apply(convertRate)

print(df)
df.rename({'listed_in(type)':'type'},axis=1,inplace=True)
print(df.info())
#
# 1) What type of restaurant do the majority of customers order from?
sns.countplot(x=df['type'])
plt.xlabel("Type of restaurant")
plt.show()

# 2 How many votes has each type of restaurant received from customers?
grouped_data = df.groupby('type')['votes'].sum()

print(grouped_data)
result = pd.DataFrame({'votes':grouped_data})
plt.plot(result,c='g',marker='o')
plt.xlabel('type')
plt.ylabel('votes')
plt.show()

# 3) What are the ratings that the majority of restaurants have received?

plt.hist(df['rate'],bins=5)
plt.title('ratings')
plt.show()

# 4)Zomato has observed that most couples order most of their food online. What is their
# average spending on each order?

count_data = df['approx_cost(for two people)']
sns.countplot(x=count_data)
plt.show()

# 5) Which mode (online or offline) has received the maximum rating?

plt.figure(figsize=(6,6))
sns.boxplot(x='online_order',y='rate',data=df)
plt.show()

# 6) Which type of restaurant received more offline orders, so that Zomato can provide those
# customers with some good offers?

heat_data = df.pivot_table(index='type',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(heat_data,annot=True,cmap="YlGnBu",fmt='d')
plt.title('heatmap')
plt.xlabel('online order')
plt.ylabel('type')
plt.show()