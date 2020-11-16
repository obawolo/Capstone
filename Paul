import pandas as pd
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report
import numpy as np
ts_df = #PLEASE READ IN YOUR DATA HERE
cleaned_df = ts_df[ts_df != np.nan].dropna()
cleaned_df.head()
x = cleaned_df[['1. open','2. high','3. low','5. volume']]
x.head()
y = cleaned_df[["4. close"]]
y.head()
 x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33,random_state=42)
#take a look at the train dataset
print (x_train)
print (y_train)
# Create linear regression object
regr = LinearRegression()
regr.fit(x_train, y_train)
predictions = regr.predict(x_test)
fig, axes = plt.subplots(2, sharex = True)
fig.suptitle('actual data vs predictions for closing balance')
axes[0].plot(y_test.index, y_test, label = "testing data")
axes[0].set_xticks(y_test.index)
axes[0].set_title('testing data')
axes[1].plot(predictions, label = "predictions")
axes[1].set_title('predictions')
plt.xlabel('x - axis')
# Set the y axis label of the current axis.
plt.ylabel('y - axis')
#plt.xticks()
# Set a title of the current axes.
plt.title('actual data vs predictions for closing balance')
# show a legend on the plot
plt.legend()
# Display a figure.
plt.show()
