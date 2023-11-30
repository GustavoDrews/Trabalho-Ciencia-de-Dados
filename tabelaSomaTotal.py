import pandas as pd

dados = pd.read_csv("covid.csv")

cases_by_country = dados.groupby('country')[[
    'cumulative_total_cases', 
    'daily_new_cases',
    'active_cases',
    'cumulative_total_deaths',
    'daily_new_deaths'
]].sum()

print(cases_by_country)