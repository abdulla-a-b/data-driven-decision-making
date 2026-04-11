import pandas as pd

data = {
"Dept":["Production","Sales","HR","Accounts"],
"Employees":[200,120,40,30],
"Resigned":[30,25,2,1]
}

df = pd.DataFrame(data)

df["Attrition"] = (df["Resigned"]/df["Employees"])*100

print(df)
