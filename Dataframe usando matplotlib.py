Esse código cria um DataFrame usando Pandas com duas séries de valores (Y1 e Y2) em função de x.
Depois, plota essas duas séries em um mesmo gráfico de linha usando o Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# Dados
dados = {'x': [1, 2, 3, 4, 5, 6],
         'Y1': [120, 110, 130, 145, 118, 125],
         'Y2': [95, 54, 86, 77, 90, 81]}

# Criando o DataFrame
base = pd.DataFrame(dados)

# Plot
fig, ax = plt.subplots()
ax.plot(base['x'], base['Y1'], label="Y1")
ax.plot(base['x'], base['Y2'], label="Y2")

# Legenda e exibição
plt.legend()
plt.show()

import pandas as pd

Importa a biblioteca Pandas, usada para manipulação e análise de dados em tabelas (DataFrames).

import matplotlib.pyplot as plt

Importa o módulo de gráficos Matplotlib.

dados = {...}

Cria um dicionário com três chaves:

'x': valores que vão no eixo x.

'Y1' e 'Y2': duas séries numéricas diferentes que serão comparadas.

base = pd.DataFrame(dados)

Converte o dicionário em um DataFrame do Pandas.

Estrutura tabular (tipo uma planilha), com colunas x, Y1, Y2.

Exemplo do DataFrame:

   x   Y1  Y2
0  1  120  95
1  2  110  54
2  3  130  86
3  4  145  77
4  5  118  90
5  6  125  81


fig, ax = plt.subplots()

Cria uma figura (fig) e um eixo (ax) para desenhar o gráfico.

subplots() é útil quando queremos mais de um gráfico na mesma figura.

ax.plot(base['x'], base['Y1'], label="Y1")

Plota os valores da coluna 'Y1' contra 'x'.

label="Y1" define o nome que aparecerá na legenda.

ax.plot(base['x'], base['Y2'], label="Y2")

Plota a segunda série (Y2) contra 'x'.

Assim temos duas linhas no mesmo gráfico.

plt.legend()

Exibe a legenda com os nomes "Y1" e "Y2".

plt.show()

Mostra o gráfico na tela.
