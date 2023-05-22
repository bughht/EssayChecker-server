import pandas as pd

df = pd.read_csv("web/database/data.csv")
print(df.iloc[:10, :])

df_recover = df.iloc[:10, :]
df_recover.to_csv("web/database/data.csv", index=False)
