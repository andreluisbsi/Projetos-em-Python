import matplotlib.pyplot as plt
import random

x = [1, 2, 5]
y = [1, 2, 5]

# Criando um grafico com uma legenda
plt.plot(x, y, label='uma legenda')

# Atribuindo um título ao gráfico
plt.title('GRAFICO')
plt.xlabel('Variável 1')
plt.ylabel('Variável 2')

# Exibindo a legenda
plt.legend()

# Exibindo o gráfico
plt.show()

Esse código usa a biblioteca Matplotlib para criar e exibir um gráfico de linha simples, com legenda, título e rótulos dos eixos.
import matplotlib.pyplot as plt

Importa o módulo pyplot da biblioteca Matplotlib e o apelida como plt.

pyplot contém funções para criar e customizar gráficos de maneira semelhante ao Matlab.

import random

Importa o módulo random da biblioteca padrão (para geração de números aleatórios).

Neste código, não é usado. Pode ser removido sem alterar o resultado.

x = [1, 2, 5]

Lista com três valores que representam os pontos no eixo x.

y = [1, 2, 5]

Lista com três valores que representam os pontos no eixo y.

Cada índice de x corresponde ao índice de y.

Ou seja: pontos plotados serão (1,1), (2,2), (5,5).

plt.plot(x, y, label='uma legenda')

Cria um gráfico de linha usando x e y.

O argumento label define a legenda que será exibida.

Por padrão, plot conecta os pontos com linhas.

plt.title('GRAFICOZINHO')

Define o título do gráfico.

plt.xlabel('Variável 1')

Define o rótulo do eixo x.

plt.ylabel('Variável 2')

Define o rótulo do eixo y.

plt.legend()

Exibe a legenda (usando o texto definido em label dentro de plt.plot).

plt.show()

Exibe o gráfico na tela.

No Jupyter Notebook/Google Colab aparece logo abaixo da célula; em scripts Python abre uma janela.
