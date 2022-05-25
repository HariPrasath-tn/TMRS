import pandas as pd

df = pd.read_csv("../program_database/Disease_symptom_dataset.csv")
symptoms = df.columns[:-1]
new_df = df.loc[df['itching'] == 1]
new_df1 = df.loc[df['skin_rash'] == 1]
new_df2 = df.loc[df['nodal_skin_eruptions'] == 1]
new_df3 = df.loc[df['acidity'] == 1]
a = list()
a.extend(list(set(new_df.loc[:, 'prognosis'])))
a.extend(list(set(new_df1.loc[:, 'prognosis'])))
a.extend(list(set(new_df2.loc[:, 'prognosis'])))
a.extend(list(set(new_df3.loc[:, 'prognosis'])))
finalize = dict()
for i in a:
    finalize[i] = a.count(i)

max_ = 0
max_val = ""

for key, value in zip(finalize.keys(), finalize.values()):
    if value > max_:
        max_ = value
        max_val = key

print(max_val)
