import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

arquivo_excel_1='1e2.xlsx'
arquivo_excel_2='3.xlsx'


df_dia_1 = pd.read_excel(arquivo_excel_1, sheet_name='dia 1')
df_dia_2 = pd.read_excel(arquivo_excel_1, sheet_name='dia 2')
df_dia_3 = pd.read_excel(arquivo_excel_2)

df_todas_as_planilhas = pd.concat([df_dia_1,df_dia_2,df_dia_3])

print(df_todas_as_planilhas ['Vendedor'])


# soma de cada vendedor
lucro_dos_vendedores=df_todas_as_planilhas.groupby(['Vendedor']).sum()

print(lucro_dos_vendedores)

relatorio_bonito = lucro_dos_vendedores.loc[:, "unidades":"preco"]

print(relatorio_bonito)

relatorio_bonito.plot(kind='bar')

plt.show()
