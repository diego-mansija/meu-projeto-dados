**Analisando Tendências de Tecnologia com Python**

Este projeto faz parte do meu portfólio de Ciência de Dados e Desenvolvimento Python. Aqui, utilizo bibliotecas fundamentais para explorar, manipular e visualizar conjuntos de dados.

## Objetivo
Analisar o comportamento de vendas de uma loja fictícia para identificar os produtos mais rentáveis.

## Tecnologias Utilizadas
- **Python 3.12**
- **Pandas**: Manipulação e tratamento de dados.
- **Numpy**: Operações matemáticas e suporte a arrays multidimensionais.
- **Matplotlib**: Criação de visualizações e gráficos estáticos.
- **Linux Mint**: Sistema operacional utilizado no desenvolvimento.

## Funcionalidades
- Limpeza de dados (Data Cleaning).
- Análise estatística descritiva.
- Geração de gráficos de barras, linhas ou dispersão.
- Exportação de relatórios em CSV/Excel.

## Estrutura do Projeto

meu-projeto-dados/
├── data/
│   └── vendas.csv          # Base de dados bruta em formato CSV
├── src/
│   └── dashboard.ipynb     # Jupyter Notebook com as análises e gráficos
├── output/
|   └── faturamento_por_categoria.png     # Saída dos gráficos gerados
├── .gitignore              # Arquivos ignorados pelo Git (ex: .venv)
├── README.md               # Documentação do projeto
└── requirements.txt        # Bibliotecas necessárias (Pandas, Matplotlib)

## Como executar
1. Clone o repositório:
    git clone [https://github.com/diego-mansija/meu-projeto-dados.git](https://github.com/diego-mansija/meu-projeto-dados.git)

2. Crie e ative o ambiente virtual:
        python3 -m venv .venv
        source .venv/bin/activate
    
3. Atualize o pip e as bibliotecas dentro do ambiente ativado, se necessário (pode evitar erros ao criar, editar e/ou instalar as dependências a partir do 'requirements.txt'):
        python -m pip install --upgrade pip
        python -m pip install numpy pandas matplotlib

4. Instale as dependências:
        pip install -r requirements.txt

5. Execute o script principal:
        python analise.py

### Principais Insights
![Faturamento por Categoria](faturamento_por_categoria.png)
![Tendência de Faturamento Mensal](tendencia_de_faturamento.png)