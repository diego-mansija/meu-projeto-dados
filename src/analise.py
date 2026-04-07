# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# %% [markdown]
# Análise de Faturamento por Categoria
#
#     Nesta etapa, agrupamos as vendas por categoria para identificar qual setor da loja gera mais receita bruta.

# %%
# %matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import os
plt.style.use('ggplot') # Um estilo limpo e moderno

# Define o caminho da pasta output
output_path = '../output'
# Cria a pasta output se ela não existir
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Carrega os dados
df = pd.read_csv('../data/vendas.csv')

# Cria uma nova coluna de Faturamento (Quantidade * Preço)
df['Faturamento'] = df['Quantidade'] * df['Preço_Unitário']

# Agrupa por Categoria e soma o Faturamento
faturamento_por_categoria = df.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)

# Cria o gráfico
plt.figure(figsize=(10, 6))
faturamento_por_categoria.plot(kind='bar', color='skyblue')

# Personaliza o gráfico
plt.title('Faturamento Total por Categoria de Produto', fontsize=14)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostra o gráfico
plt.tight_layout()

# Define o nome do arquivo dentro da pasta output
nome_arquivo = os.path.join(output_path, 'faturamento_por_categoria.png')

# Salva a imagem com alta resolução (dpi) e ajuste de bordas (bbox_inches)
plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')

print(f"Gráfico salvo com sucesso em: {nome_arquivo}")

# Mostra na tela do VS Code após salvar
plt.show()

# (Opcional) Salvar o gráfico em PNG
# plt.savefig('faturamento_categorias.png')

# %% [markdown]
# Observamos que a categoria Hardware lidera o faturamento, apesar de ter menos transações que Acessórios. Isso indica que produtos de alto valor agregado são o motor financeiro da empresa.

# %%
# Converte a coluna Data para o formato datetime do Pandas
df['Data'] = pd.to_datetime(df['Data'])

# Agrupa faturamento por mês
vendas_mensais = df.resample('ME', on='Data')['Faturamento'].sum()

# Cria gráfico de linha
plt.figure(figsize=(12, 5))
vendas_mensais.plot(marker='o', color='green', linestyle='-')

plt.title('Tendência de Faturamento Mensal (2024)', fontsize=14)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Faturamento Total (R$)', fontsize=12)
plt.grid(True, alpha=0.3)

# Define o nome do arquivo dentro da pasta output
nome_arquivo = os.path.join(output_path, 'tendencia_de_faturamento.png')

# Salva a imagem com alta resolução (dpi) e ajuste de bordas (bbox_inches)
plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight')
print(f"Gráfico salvo com sucesso em: {nome_arquivo}")
plt.show()
