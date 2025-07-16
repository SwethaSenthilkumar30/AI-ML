import numpy as np
import pandas as pd
np.random.seed(42)
employee_ids=[f"EMP_{i:03d}"for i in range(1,31)]
dates=pd.date_range("2025-07-01",periods=30,freq="D")
print(employee_ids)
print(dates)
dates={
    "Date":np.tile(dates,len(employee_ids)),
    "Employee_ID":np.repeat(employee_ids,len(dates)),
    "Working_Hours":np.random.uniform(4,10,size=len(dates)*len(employee_ids)).round(2)
      }
df= pd.DataFrame(dates)
df.to_csv("employee_working_hours.csv",index=False)
print(dates)
df=pd.read_csv("employee_working_hours.csv")
print(df.head(5))
print(df.describe())
print(df.nunique())
total_hours=df.groupby("Employee_ID")["Working_Hours"].sum().sort_values(ascending=False)
print(total_hours)
avg_daily=df.groupby("Employee_ID")["Working_Hours"].mean()
threshold_low=5
threshold_high=9
df["Low_Hour_Flag"]=df["Working_Hours"]<threshold_low
df["High_Hour_Flag"]=df["Working_Hours"]>threshold_high
print(df[["Employee_ID", "Working_Hours", "Low_Hour_Flag"]].head())
print(df[["Employee_ID", "Working_Hours", "High_Hour_Flag"]].head())
print(avg_daily)
import seaborn as sns
import matplotlib.pyplot as plt

top10=total_hours.head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top10.index,y=top10.values)
plt.xticks(rotation=45)
plt.title("Top 10 Employees By Total Working Hours")
plt.ylabel("Hours")
plt.tight_layout()
plt.show()