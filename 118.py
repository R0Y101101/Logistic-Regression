import pandas as pd
import plotly.express as px

df = pd.read_csv("logistics_data.csv")

estimated_salary = df["EstimatedSalary"].tolist()
purschased = df["Purchased"].tolist()

fig = px.scatter(x=estimated_salary, y=purschased)
fig.show()

import plotly.graph_objects as go

ages = df["Age"].tolist()
salaries = df["EstimatedSalary"].tolist()

purchased = df["Purchased"].tolist()

colors = []

for data in purchased:
    if data == 1:
        colors.append("green")
    else:
        colors.append("red")

fig = go.Figure(data=go.Scatter(
    x=salaries,
    y=ages,
    mode="markers",
    marker = dict(color=colors)
))
fig.show()
