import pandas as pd
import plotly.express as px

df = pd.read_csv("data_classification.csv")

hours_slept = df["Hours_Slept"].tolist()
hours_studied = df["Hours_studied"].tolist()

fig = px.scatter(x=hours_slept, y=hours_studied)
fig.show()

import plotly.graph_objects as go


hours_slept = df["Hours_Slept"].tolist()
hours_studied = df["Hours_studied"].tolist()


results = df["results"].tolist()
colors=[]
for data in results:
 if data == 1:
   colors.append("green")
 else:
   colors.append("red")


fig = go.Figure(data=go.Scatter(
   x=hours_slept,
   y=hours_studied,
   mode='markers',
   marker=dict(color=colors)
))
fig.show()

#hours studies and slept of the person
hours = df[["Hours_studied", "Hours_Slept"]]

#results
results = df["results"]


from sklearn.model_selection import train_test_split 

hours_train, hours_test, results_train, results_test = train_test_split(hours, results, test_size = 0.25, random_state = 0)

print(hours_train[0:10])

print(hours_train[0:10])

from sklearn.preprocessing import StandardScaler 
sc_x = StandardScaler() 

hours_train = sc_x.fit_transform(hours_train)  
hours_test = sc_x.transform(hours_test) 
  
print(hours_train[0:10])

from sklearn.linear_model import LogisticRegression 

classifier = LogisticRegression(random_state = 0) 
classifier.fit(hours_train, results_train)

results_pred = classifier.predict(hours_test)

from sklearn.metrics import accuracy_score 
print ("Accuracy : ", accuracy_score(results_test, results_pred)) 


user_hours_studied = int(input("Enter hours studied -> "))
user_hours_slept = int(input("Enter hours slept -> "))

#we are transforming the values here
user_test = sc_x.transform([[user_hours_studied, user_hours_slept]])

#predicting the values using the function.
user_result_pred = classifier.predict(user_test)

if user_result_pred[0] == 1:
  print("This user may pass!")
else:
  print("This user may not pass!")

