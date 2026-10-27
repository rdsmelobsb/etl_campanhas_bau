import pandas as pd

caminho = 'V2 - GESTAO DE CAMPANHAS - VERSAO FINAL(Taxonomia BAU) (3).csv'

df = pd.read_csv(caminho, sep=';', encoding='utf-8', low_memory=False)

df = df[df.columns[1:14]]

df = df[df['Data'].str.contains('10/2025', na=False) | df['Data'].str.contains('10/2026', na=False)]

df = df[df['Campanhas'].str.contains('beleza', case=False, na=False)]

df.to_excel('campanhas.xlsx', index=False)

print("Tarefa concluída!")
