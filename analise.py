import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Define o motor de janelas antes de importar o pyplot
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv('vendas.csv')

# Criar uma nova coluna de Faturamento (Quantidade * Preço)
df['Faturamento'] = df['Quantidade'] * df['Preço_Unitário']

# Agrupar por Categoria e somar o Faturamento
faturamento_por_categoria = df.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)

# Criar o gráfico
plt.figure(figsize=(10, 6))
faturamento_por_categoria.plot(kind='bar', color='skyblue')

# Personalizar o gráfico (importante para o portfólio!)
plt.title('Faturamento Total por Categoria de Produto', fontsize=14)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Faturamento (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar o gráfico
plt.tight_layout()
plt.show()

# (Opcional) Salvar o gráfico para usar no README
# plt.savefig('faturamento_categorias.png')