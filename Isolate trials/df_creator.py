import pandas as pd


df = pd.read_excel('PDF_Extract\Comprovantes de pagamento.xlsx', usecols='B, C')

# print(df.head())

df2=df.loc[df(['Chave'] == 597.68217), 'Imóvel'].iloc[0]
print(df2)



