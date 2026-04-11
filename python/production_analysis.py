import pandas as pd

df = pd.read_csv("../data/production.csv")

df["Gap"] = df["Target"] - df["Actual"]
df["Efficiency"] = (df["Actual"] / df["Target"]) * 100

problem = df.loc[df["Gap"].idxmax()]

print("=== DATA DRIVEN DECISION ===")
print("Problem Section:", problem["Section"])
print("Efficiency:", round(problem["Efficiency"],2))

print("\nFull Analysis")
print(df)
