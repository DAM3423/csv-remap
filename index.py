import pandas as pd

df = pd.read_csv('train.csv')

# Rename columns
#   PassengerId  ->  Id
#   Pclass       ->  Class
df.rename(
    columns=({'PassengerId': 'Id', 'Pclass': 'Class'}),
    inplace=True,
)

df.to_csv('output.csv')
