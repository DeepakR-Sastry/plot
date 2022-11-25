import pandas as pd
import plotly.express as px
df = pd.read_csv("gpu_utilization.csv")
for key, value in df.items() :
    print (key, value)
fig = px.line(df, x=df["timestamp"], y =df[" utilization"], title='Apple Share Prices over time (2014)')
fig.show()