import pandas as pd
from IPython.display import display

#Faturamento Total
tabela = pd.read_excel("Vendas.xlsx")
#display(tabela)
total_faturamento = tabela["Valor Final"].sum()
#print(total_faturamento)

#faturamento por loja
faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
#display(faturamento_por_loja)
faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()
display(faturamento_por_produto)