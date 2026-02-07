import pandas as pd
import matplotlib.pyplot as plt

# Unemployment data
url_unrate = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=UNRATE"
unemp = pd.read_csv(url_unrate)
unemp.columns = ["Date", "Unemployment"]
unemp["Date"] = pd.to_datetime(unemp["Date"])

# Inflation data (CPI)
url_cpi = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCSL"
cpi = pd.read_csv(url_cpi)
cpi.columns = ["Date", "CPI"]
cpi["Date"] = pd.to_datetime(cpi["Date"])

# Merge both datasets on Date
df = pd.merge(unemp, cpi, on="Date")

print(df.head())

df["Inflation"] = df["CPI"].pct_change() * 100
print (df[["Date", "Unemployment", "Inflation"]].head())

plt.scatter(df["Unemployment"],  df ["Inflation"])
plt.title("Unemployment vs Inflation (Phillips Curve)")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Inflation Rate (%)")
plt.show()