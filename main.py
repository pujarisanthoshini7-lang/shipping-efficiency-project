import pandas as pd
import numpy as np

n = 500

df = pd.DataFrame({
    "Order Date": pd.date_range(start="2023-01-01", periods=n),
})

df["Ship Date"] = df["Order Date"] + pd.to_timedelta(np.random.randint(1, 7, n), unit='D')

df["State"] = np.random.choice(["CA", "TX", "NY", "FL"], n)
df["Region"] = np.random.choice(["West", "South", "East"], n)
df["Ship Mode"] = np.random.choice(["Standard", "Express"], n)
df["Factory"] = np.random.choice(["Factory A", "Factory B"], n)

print(df.head())
df["Lead Time"] = (df["Ship Date"] - df["Order Date"]).dt.days

print(df.head())
print(df.groupby("State")["Lead Time"].mean())
import matplotlib.pyplot as plt

df.groupby("State")["Lead Time"].mean().plot(kind="bar")

plt.title("Average Shipping Time by State")
plt.xlabel("State")
plt.ylabel("Days")

plt.show()
df.to_csv("final_data.csv", index=False)
df.to_excel("final_data.xlsx", index=False)
print("Excel file saved")