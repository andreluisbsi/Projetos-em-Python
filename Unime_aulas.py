{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPGNR9O541DO/hrnaMp/4YQ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/andreluisbsi/Aula-de-engenharia/blob/main/Unime_aulas.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NglwiAj7rZ-I",
        "outputId": "869d3acd-eab8-4546-9ffb-de9a62a14852"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "O resultado da sua soma é:  13\n"
          ]
        }
      ],
      "source": [
        "def soma(a,b):\n",
        "  resultado = a + b\n",
        "  return resultado\n",
        "\n",
        "resultado_soma = soma(10,3)\n",
        "print(\"O resultado da sua soma é: \", resultado_soma)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import random\n",
        "\n",
        "x = [1, 2, 5]\n",
        "y = [1, 2, 5]\n",
        "\n",
        "# Criando um grafico com uma legenda\n",
        "plt.plot(x, y, label='uma legenda')\n",
        "\n",
        "# Atribuindo um título ao gráfico\n",
        "plt.title('GRAFICOZINHO')\n",
        "plt.xlabel('Variável 1')\n",
        "plt.ylabel('Variável 2')\n",
        "\n",
        "# Exibindo a legenda\n",
        "plt.legend()\n",
        "\n",
        "# Exibindo o gráfico\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "-suyKJ2MDmwa",
        "outputId": "295a7fc2-ae77-4a1c-e008-57735fbae042"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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QWpqKklJSVd9kML/feieOXOGqVOncuTIEcqVK5evzcWLF1m6dCmDBg3KdxXk3nvvZeHChRw4cICGDRvm28bf358OHToUuA9XPvivfLjfjKen503bXi8onDt3jvDwcCpWrMjs2bNxcLi1i9r3338/7dq144MPPuCFF164adsqVapctdzNzS3f+yu1pqamUqFChWvuqyABSKQs0bCUiB3y9vamevXqxMXFXbWuRYsWdOjQgXvvvfea295///106NCB8PBwVqxYQbly5ejXr1++uSDz588nMzOTSZMm4e/vn/caOnQoQJFMLA4MDAQgNja2QO0bNWrE/v37yczMvG6bXbt24ezsjL+/f94ywzAYMGAAJ0+eZNasWdSoUeO26h49ejSJiYnMmDHjtvZzRaNGjQDy3ZPo766sa9y4cZEcU8TWKdyI2KmuXbsSHx/P77//fsv78PDwYPTo0cTExDBv3ry85bNnz6Zp06bMnz//qleHDh2IjIy87frvu+8+KlasyJw5c8jNzb1p+27dupGRkcH8+fOvuf7o0aOsX7+eBx54IN+VqA8//JCff/6ZIUOG0LVr19uuu02bNrRt27bIvr105YZ+33zzzTXX5+bmEhkZScWKFa8bWEXKGoUbETs1YsQI3N3deeaZZ0hKSrpqvVHAu9r269ePWrVq8f777wNw/Phx1q1bR69evXj88cevej399NPEx8ezdevW26rf3d2dkSNHsnfvXkaOHHnNev/3v//lhbfnn3+eatWqMXz4cA4fPpyvXUZGBk8//TSGYfDWW2/lLd+2bRujRo2iefPmvPfee7dV71+NGTOGxMREPv/889veV6tWrejQoQMzZ85kyZIlV63/97//zYEDBxgxYsRVw4ciZZXm3IjYKX9/fyIjIwkPDycgICDvDsWGYXDkyBEiIyNxcHCgVq1aN9yPs7MzgwcPZvjw4SxbtoydO3diGMY177kC0KVLF5ycnJg9e/Ztfw19+PDh7N69m0mTJrF69Woef/xxfH19SUxMZPHixfz+++9s2rQJgMqVK7NgwQK6du1KWFjYVXcojo+PZ8qUKXl3M7506RK9e/cmOzubbt265bsy9Vc+Pj48+OCDhaq7TZs2tGnThrVr195W/6/45ptvaN++PY888gh9+/aldevWZGZm8v3337NmzRp69+7N8OHDi+RYInbBzDsIikjxi4+PN1588UWjQYMGhpubm1GuXDkjMDDQeOGFF4yYmJi8dje6c25ycrLh7e1ttGnTxggKCjJq1659w2O2bdvWqFatmpGdnX1bdyi+YsGCBUbHjh2NSpUqGU5OTkb16tWN3r17G2vWrLmq7ZEjR4znnnvOqF27tuHs7GxUqVLFePjhh43169df1Q646atNmzZ521zvDsURERFX1bF69eq8fdzuHYoNwzBSU1ONMWPGGE2aNDHKlStneHp6Gvfee68xa9asa969WaQssxiGnrgmIiIi9kNzbkRERMSuKNyIiIiIXVG4EREREbuicCMiIiJ2ReFGRERE7IrCjYiIiNiVMncTP6vVysmTJ/H09MRisZhdjoiIiBSAYRikpqZSo0aNmz7ctsyFm5MnT+Ln52d2GSIiInILjh8/ftM7q5e5cOPp6Qn8+Y/j5eVlcjUiIiJSECkpKfj5+eV9jt9ImQs3V4aivLy8FG5ERERsTEGmlGhCsYiIiNgVhRsRERGxKwo3IiIiYlfK3JybgsrNzSU7O9vsMqSUc3FxuelXEkVEpGQp3PyNYRgkJiZy8eJFs0sRG+Dg4EC9evVwcXExuxQREfn/FG7+5kqwqVatGu7u7rrRn1zXlRtCnjp1itq1a+tnRUSklFC4+Yvc3Ny8YFO5cmWzyxEbULVqVU6ePElOTg7Ozs5mlyMiImhCcT5X5ti4u7ubXInYiivDUbm5uSZXIiIiVyjcXIOGF6Sg9LMiIlL6KNyIiIiIXTE13IwZMwaLxZLvFRgYeMNt5s+fT2BgIG5ubgQFBbF06dISqlYKasyYMYSEhJhdRoFZLBYWL15sdhkiIlJETL9y06RJE06dOpX32rBhw3Xbbtq0ifDwcAYOHEh0dDQ9evSgR48exMXFlWDFIiIiUpqZHm6cnJzw9fXNe1WpUuW6badMmcJDDz3E8OHDadSoEePGjSMsLIxp06aVYMUiIiJyPTuOXeBcWqapNZgebg4ePEiNGjWoX78+/fr1IyEh4bptN2/eTIcOHfIt69SpE5s3b77uNpmZmaSkpOR72aO6devy0Ucf5VsWEhLCmDFj8t5bLBZmzJhBt27dcHd3p1GjRmzevJn4+Hjatm1L+fLladWqFYcOHcrb5tChQzzyyCP4+Pjg4eHBXXfdxW+//Vbo+r788ksaNWqEm5sbgYGBfPLJJ/nWb9q0iZCQENzc3LjzzjtZvHgxFouFmJiYvDZxcXF07twZDw8PfHx8ePLJJzl79mze+rZt2/Lyyy8zYsQIKlWqhK+vb77+w58/b/fffz9ubm40btyYFStWXFXryJEjadiwIe7u7tSvX58333xTd6sWEbkJq9Xgs7WH6DVjM6/O34nVaphWi6nhpkWLFsyaNYtly5bx6aefcuTIEVq3bk1qauo12ycmJuLj45NvmY+PD4mJidc9xvjx4/H29s57+fn5FapGwzC4lJVjysswiv4HY9y4cfTv35+YmBgCAwPp27cvzz//PKNGjWL79u0YhsGgQYPy2qelpdGlSxdWrlxJdHQ0Dz30EN27d79hCP272bNn89Zbb/HOO++wd+9e3n33Xd58802+/vprAFJSUujevTtBQUFERUUxbtw4Ro4cmW8fFy9e5IEHHiA0NJTt27ezbNkykpKS6NWrV752X3/9NeXLl2fr1q188MEHvP3223kBxmq18thjj+Hi4sLWrVv57LPPrjoOgKenJ7NmzWLPnj1MmTKFL774gsmTJxe4vyIiZc25tEye+Xob7/2yj1yrgaebM1m5VtPqMfUmfp07d87772bNmtGiRQvq1KnDvHnzGDhwYJEcY9SoUQwdOjTvfUpKSqECzuXsXBq/tbxIaimsPW93wt2laE/R008/nRcIRo4cScuWLXnzzTfp1KkTAIMHD+bpp5/Oax8cHExwcHDe+3HjxrFo0SJ+/PHHfCHoRkaPHs2kSZN47LHHAKhXrx579uxhxowZDBgwgMjISCwWC1988UXeFZU//viD5557Lm8f06ZNIzQ0lHfffTdv2VdffYWfnx8HDhygYcOGwJ8/R6NHjwbA39+fadOmsXLlSh588EF+++039u3bx/Lly6lRowYA7777br6fQ4A33ngj77/r1q3LsGHDmDt3LiNGjChQf0VEypKth8/x8txoklIycXVyYMzDTehzl5+pt8ooVXcorlChAg0bNiQ+Pv6a6319fUlKSsq3LCkpCV9f3+vu09XVFVdX1yKt05Y1a9Ys77+vXAULCgrKtywjI4OUlBS8vLxIS0tjzJgx/Pzzz5w6dYqcnBwuX75c4Cs36enpHDp0iIEDB+YLKzk5OXh7ewOwf/9+mjVrhpubW976u+++O99+du7cyerVq/Hw8LjqGIcOHcoXbv6qevXqnD59GoC9e/fi5+eX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KxpffvnlNdfZ8rn7qxv10VbPX2pqquHv72+sWLHCaNOmjTF48ODrtrXF81iY/tnaORw9erQRHBxc4PZmnT9duSkmmzdvpkOHDvmWderUic2bN5tUUfEJCQmhevXqPPjgg2zcuNHscgosOTkZgEqVKl23jS2fx4L0DyAtLY06derg5+d306sEpUVubi5z584lPT2dli1bXrONLZ87KFgfwTbPX0REBF27dr3q/FyLLZ7HwvQPbO8cHjx4kBo1alC/fn369etHQkLCdduadf7K3IMzS0piYiI+Pj75lvn4+JCSksLly5cpV66cSZUVnerVq/PZZ59x5513kpmZyZdffknbtm3ZunUrYWFhZpd3Q1arlSFDhnDvvffStGnT67a73nksrfOKriho/wICAvjqq69o1qwZycnJTJw4kVatWrF79+5if8DsrYiNjaVly5ZkZGTg4eHBokWLaNy48TXb2uq5K0wfbe38AcydO5eoqCi2bdtWoPa2dh4L2z9bO4ctWrRg1qxZBAQEcOrUKcaOHUvr1q2Ji4vD09PzqvZmnT+FG7llAQEBBAQE5L1v1aoVhw4dYvLkyXz77bcmVnZzERERxMXF3XCs2JYVtH8tW7bMd1WgVatWNGrUiBkzZjBu3LjiLrPQAgICiImJITk5mQULFjBgwADWrl173Q9/W1SYPtra+Tt+/DiDBw9mxYoVpXrS7K26lf7Z2jns3Llz3n83a9aMFi1aUKdOHebNm8fAgQNNrCw/hZti4uvrS1JSUr5lSUlJeHl52cVVm+u5++67S31gGDRoEEuWLGHdunU3/cvoeufR19e3OEu8LYXp3985OzsTGhpKfHx8MVV3e1xcXGjQoAEAzZs3Z9u2bUyZMoUZM2Zc1dYWzx0Uro9/V9rP344dOzh9+nS+K7u5ubmsW7eOadOmkZmZiaOjY75tbOk83kr//q60n8O/q1ChAg0bNrxuvWadP825KSYtW7Zk5cqV+ZatWLHihmPn9iAmJobq1aubXcY1GYbBoEGDWLRoEatWraJevXo33caWzuOt9O/vcnNziY2NLbXn8O+sViuZmZnXXGdL5+5GbtTHvyvt5699+/bExsYSExOT97rzzjvp168fMTEx1/zgt6XzeCv9+7vSfg7/Li0tjUOHDl23XtPOX7FOV7YjqampRnR0tBEdHW0AxocffmhER0cbx44dMwzDMF577TXjySefzGt/+PBhw93d3Rg+fLixd+9eY/r06Yajo6OxbNkys7pwU4Xt4+TJk43FixcbBw8eNGJjY43BgwcbDg4Oxm+//WZWF27oxRdfNLy9vY01a9YYp06dyntdunQpr82TTz5pvPbaa3nvN27caDg5ORkTJ0409u7da4wePdpwdnY2YmNjzejCDd1K/8aOHWssX77cOHTokLFjxw6jT58+hpubm7F7924zunBDr732mrF27VrjyJEjxq5du4zXXnvNsFgsxq+//moYhm2fuysK20dbOn/X8/dvE9nDefyrm/XP1s7hq6++aqxZs8Y4cuSIsXHjRqNDhw5GlSpVjNOnTxuGUXrOn8JNAV352vPfXwMGDDAMwzAGDBhgtGnT5qptQkJCDBcXF6N+/frGzJkzS7zuwihsH99//33jjjvuMNzc3IxKlSoZbdu2NVatWmVO8QVwrb4B+c5LmzZt8vp7xbx584yGDRsaLi4uRpMmTYyff/65ZAsvoFvp35AhQ4zatWsbLi4uho+Pj9GlSxcjKiqq5IsvgGeeecaoU6eO4eLiYlStWtVo37593oe+Ydj2ubuisH20pfN3PX//8LeH8/hXN+ufrZ3D3r17G9WrVzdcXFyMmjVrGr179zbi4+Pz1peW82cxDMMo3mtDIiIiIiVHc25ERETErijciIiIiF1RuBERERG7onAjIiIidkXhRkREROyKwo2IiIjYFYUbEbF5y5cvZ9asWWaXISKlhMKNiNgEi8XC4sWLr1q+b98+nn32WVq0aFHkx2zbti1Dhgwp8v2KSPFSuBGRItG9e3ceeuiha65bv349FouFXbt23fL+T506le+JxAAZGRn079+f//3vfzRq1OiW9307NfXt25eGDRvi4OCgICRSSijciEiRGDhwICtWrODEiRNXrZs5cyZ33nknzZo1K/R+s7KygD+fLuzq6ppvnZubG7///jtt2rS5taJvU2ZmJlWrVuWNN94gODjYlBpE5GoKNyJSJLp160bVqlWvmvuSlpbG/PnzGThwIOfOnSM8PJyaNWvi7u5OUFAQc+bMyde+bdu2DBo0iCFDhlClShU6deoEXD0sNXLkSBo2bIi7uzv169fnzTffJDs7G4ADBw5gsVjYt29fvn1PnjyZO+64I+99XFwcnTt3xsPDAx8fH5588knOnj1b4D7XrVuXKVOm0L9/f7y9vQu8nYgUL4UbESkSTk5O9O/fn1mzZvHXR9bNnz+f3NxcwsPDycjIoHnz5vz888/ExcXxz3/+kyeffJLff/89376+/vprXFxc2LhxI5999tk1j+fp6cmsWbPYs2cPU6dO5b///S+TJ08GoGHDhtx5553Mnj073zazZ8+mb9++AFy8eJEHHniA0NBQtm/fzrJly0hKSqJXr15F+c8iImYo9kdzikiZsXfvXgMwVq9enbesdevWxhNPPHHdbbp27Wq8+uqree/btGljhIaGXtUOMBYtWnTd/UycONFo3rx53vvJkycbd9xxR977/fv3G4Cxd+9ewzAMY9y4cUbHjh3z7eP48eMGYOzfvz+vlr8+0flGCtNWRIqXrtyISJEJDAykVatWfPXVVwDEx8ezfv16Bg4cCEBubi7jxo0jKCiISpUq4eHhwfLly0lISMi3n+bNm9/0WF9//TUhISF4eHhgsVgYNmxYvv306dOHo0ePsmXLFuDPqzZhYWEEBgYCsHPnTlavXo2Hh0fe68q6Q4cO3f4/hoiYRuFGRIrUwIEDWbhwIampqcycOZM77rgjb8LvhAkTmDJlCiNHjmT16tXExMTQqVOnvEnDV5QvX/6Gx9iwYQPPPvssw4cP5/jx41itVj755JN8+/H19eWBBx4gMjISgMjISPr165e3Pi0tje7duxMTE5PvdfDgQe6///6i+ucQERMo3IhIkerVqxcODg5ERkbyzTff8Mwzz2CxWADYuHEjjzzyCE888QTBwcHUr1+fAwcOFPoYW7ZsoW7duvTr14+KFStisVjYtGnTVe369evHd999x+bNmzl8+DB9+vTJWxcWFsbu3bupW7cuDRo0yPe6WbgSkdJN4UZEipSHhwe9e/dm1KhRnDp1iqeeeipvnb+/PytWrGDTpk3s3buX559/nqSkpEIfIyAggMOHDzN79mwOHTrEhx9+yNKlS69q99hjj5GamsqLL75Iu3btqFGjRt66iIgIzp8/T3h4ONu2bePQoUMsX76cp59+mtzc3ALXcuWKT1paGmfOnCEmJoY9e/YUuk8iUnQUbkSkyA0cOJALFy7QqVOnfIHijTfeICwsjE6dOtG2bVt8fX3p0aNHofffvXt3RowYwZAhQwgJCeH333/nzTffvKqdp6cn3bt3Z+fOnfmGpABq1KjBxo0byc3NpWPHjgQFBTFkyBAqVKiAg0PBfzWGhoYSGhrKjh07iIyMJDQ0lC5duhS6TyJSdCyG8ZfvbIqIiIjYOF25EREREbuicCMiIiJ2ReFGRERE7IrCjYiIiNgVhRsRERGxKwo3IiIiYlcUbkRERMSuKNyIiIiIXVG4EREREbuicCMiIiJ2ReFGRERE7IrCjYiIiNiV/wd4It/+pPWI6wAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "dados = { 'x': [1,2,3,4,5,6],\n",
        "         'Y1': [120,110,130,145,118,125],\n",
        "         'Y2': [95,54,86,77,90,81] }\n",
        "base = pd.DataFrame(dados)\n",
        "#plot\n",
        "\n",
        "fig, ax = plt.subplots()\n",
        "ax.plot(base.[X],base.Y1, label=\"Y1\")\n",
        "ax.plot(base.[X],base.Y2, label=\"Y2\")\n",
        "\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "ve5rxioyJvwH",
        "outputId": "5a4614cb-d279-45ae-8d0c-fa4b81348222"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-11-01cc115ee974>, line 10)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-11-01cc115ee974>\"\u001b[0;36m, line \u001b[0;32m10\u001b[0m\n\u001b[0;31m    ax.plot(base.[X],base.Y1, label=\"Y1\")\u001b[0m\n\u001b[0m                 ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "# Dados\n",
        "dados = {'x': [1, 2, 3, 4, 5, 6],\n",
        "         'Y1': [120, 110, 130, 145, 118, 125],\n",
        "         'Y2': [95, 54, 86, 77, 90, 81]}\n",
        "\n",
        "# Criando o DataFrame\n",
        "base = pd.DataFrame(dados)\n",
        "\n",
        "# Plot\n",
        "fig, ax = plt.subplots()\n",
        "ax.plot(base['x'], base['Y1'], label=\"Y1\")\n",
        "ax.plot(base['x'], base['Y2'], label=\"Y2\")\n",
        "\n",
        "# Legenda e exibição\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "GG0kOE4NK3S8",
        "outputId": "c9aacbdc-244b-4eee-f447-c8faa163c712",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Lista para armazenar convidados\n",
        "convidados = []\n",
        "\n",
        "# Coletar convidados\n",
        "while True:\n",
        "    nome = input(\"Quem você quer convidar? (ou digite 'fim' para encerrar) \")\n",
        "    if nome.lower() == 'fim':\n",
        "        break\n",
        "    convidados.append(nome)\n",
        "\n",
        "# Listas para presença e ausência\n",
        "presentes = []\n",
        "ausentes = []\n",
        "\n",
        "# Coletar confirmações\n",
        "while True:\n",
        "    nome = input(\"Quem está presente? (ou digite 'fim' para encerrar) \")\n",
        "    if nome.lower() == 'fim':\n",
        "        break\n",
        "    if nome in convidados:\n",
        "        presentes.append(nome)\n",
        "    else:\n",
        "        print(f\"{nome} não está na lista de convidados.\")\n",
        "\n",
        "# Identificar ausentes\n",
        "ausentes = [convidado for convidado in convidados if convidado not in presentes]\n",
        "\n",
        "# Exibir resultados\n",
        "print(\"\\nConvidados presentes:\")\n",
        "for pessoa in presentes:\n",
        "    print(f\"- {pessoa}\")\n",
        "\n",
        "print(\"\\nConvidados ausentes:\")\n",
        "for pessoa in ausentes:\n",
        "    print(f\"- {pessoa}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j9X2Oi5-_-Y_",
        "outputId": "8b22fd0d-6cee-4e13-def2-80643cd7528b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quem você quer convidar? (ou digite 'fim' para encerrar) andre, bruno, vitor, iago\n",
            "Quem você quer convidar? (ou digite 'fim' para encerrar) fim\n",
            "Quem está presente? (ou digite 'fim' para encerrar) andre, bruno, vitor\n",
            "andre, bruno, vitor não está na lista de convidados.\n",
            "Quem está presente? (ou digite 'fim' para encerrar) fim\n",
            "\n",
            "Convidados presentes:\n",
            "\n",
            "Convidados ausentes:\n",
            "- andre, bruno, vitor, iago\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Lista para armazenar convidados\n",
        "convidados = []\n",
        "\n",
        "# Coletar convidados\n",
        "while True:\n",
        "    nome = input(\"Quem você quer convidar? (ou digite 'fim' para encerrar) \")\n",
        "    if nome.lower() == 'fim':\n",
        "        break\n",
        "    convidados.append(nome)\n",
        "\n",
        "# Coletar confirmações\n",
        "confirmados = []\n",
        "while True:\n",
        "    nome = input(\"Quem confirmou? (ou digite 'fim' para encerrar) \")\n",
        "    if nome.lower() == 'fim':\n",
        "        break\n",
        "    confirmados.append(nome)\n",
        "\n",
        "# Identificar convidados que não confirmaram\n",
        "nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]\n",
        "\n",
        "# Exibir resultado\n",
        "print(\"\\nConvidados que ainda não confirmaram:\")\n",
        "if nao_confirmados:\n",
        "    for pessoa in nao_confirmados:\n",
        "        print(f\"- {pessoa}\")\n",
        "else:\n",
        "    print(\"Todos os convidados confirmaram!\")\n",
        "\n",
        "print(\"\\nEnviar lembretes para os convidados que não confirmaram.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FAl9WnrQCHz2",
        "outputId": "58b35a7a-f33b-4af8-b61d-34cedce89116"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quem você quer convidar? (ou digite 'fim' para encerrar) andre, bruno, vitor e iago\n",
            "Quem você quer convidar? (ou digite 'fim' para encerrar) fim\n",
            "Quem confirmou? (ou digite 'fim' para encerrar) andre, bruno\n",
            "Quem confirmou? (ou digite 'fim' para encerrar) fim\n",
            "\n",
            "Convidados que ainda não confirmaram:\n",
            "- andre, bruno, vitor e iago\n",
            "\n",
            "Enviar lembretes para os convidados que não confirmaram.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def e_par (numero):\n",
        "  if numero %2 == 0:\n",
        "    return True\n",
        "  else:\n",
        "    return False\n",
        "  numero = 45454\n",
        "if e_par(numero):\n",
        "     print({numero}\"seu numero é par\")\n",
        "else:\n",
        "    print({numero}\"seu numero é impar\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        },
        "id": "wbs9_0nRted3",
        "outputId": "68860367-4dae-48c5-d2c3-dee206a110ad"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax. Perhaps you forgot a comma? (<ipython-input-24-898864850a4d>, line 8)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-24-898864850a4d>\"\u001b[0;36m, line \u001b[0;32m8\u001b[0m\n\u001b[0;31m    print({numero}\"seu numero é par\")\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax. Perhaps you forgot a comma?\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "texto =  \"explorando a linguegem Python\"\n",
        "\n",
        "print(f\"Tamanho do texto = {len(texto)}\")\n",
        "print(f\"Python in texto = {'Python' in texto}\")\n",
        "print(f\"Quantidade de e no texto = {texto.count('e')}\")\n",
        "print(f\"As 5 primeiras letras são: {texto[:5]}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fnovVppI7Ic4",
        "outputId": "ed1b7cad-0959-4576-d219-35b007524db3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Tamanho do texto = 29\n",
            "Python in texto = True\n",
            "Quantidade de e no texto = 3\n",
            "As 5 primeiras letras são: explo\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nomes = [\"Andre\", \"Fernanda\", \"Taisla\", \"Edina\", \"Alice\"]\n",
        "print(\"Antes da listcomp =\", nomes)\n",
        "nomes = [item.lower() for item in nomes]\n",
        "print(\"\\nDepois da listcomp = \", nomes)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GMpHJLaF863V",
        "outputId": "11df891d-1aab-486c-b740-527a31d65a5c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Antes da listcomp = ['Andre', 'Fernanda', 'Taisla', 'Edina', 'Alice']\n",
            "\n",
            "Depois da listcomp =  ['andre', 'fernanda', 'taisla', 'edina', 'alice']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Funçaõ map\n",
        "#Aplica a uma função em toda a sequencia\n",
        "#map(funcao, sequencia)\n",
        "precos_em_dolares = float(input(\"Digite o valor em dolares: \"))\n",
        "taxa_de_cambio = float(input(\"Digite o valor da taxa de cambio do dia: \"))\n",
        "precos_em_reais = precos_em_dolares * taxa_de_cambio\n",
        "print(precos_em_reais)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LuaciJRt9ePf",
        "outputId": "03752f19-b3e9-4e91-aac8-ee8e0323e143"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o valor em dolares: 3.5\n",
            "Digite o valor da taxa de cambio do dia: 6.5\n",
            "22.75\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#lista de convidados\n",
        "convidados = []\n",
        "nomes = str(input(\"Quem você quer convidar? \"))\n",
        "convidados.append(nomes)\n",
        "confirmados = []\n",
        "confirmados_nomes = str(input(\"Quem confirmou? \"))\n",
        "confirmados.append(confirmados_nomes)\n",
        "nao_confirmados = [convidados for convidados in convidados if convidados not in confirmados]\n",
        "print(\"Convidados que ainda não confirmaram: \")\n",
        "for pessoa in nao_confirmados:\n",
        "    print(pessoa)\n",
        "print(\"\\nEnviar lembretes para os convidados que nao confirmaram.\")\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "SnyBVRWI9eox",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "89087423-2ef5-43b5-a395-03f8cd3c3996"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quem você quer convidar? jose, paula\n",
            "Quem confirmou? paula\n",
            "Convidados que ainda não confirmaram: \n",
            "jose, paula\n",
            "\n",
            "Enviar lembretes para os convidados que nao confirmaram.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Lista para armazenar convidados\n",
        "convidados = []\n",
        "\n",
        "# Adiciona convidados\n",
        "while True:\n",
        "    nome = input(\"Quem você quer convidar? (ou digite 'fim' para encerrar) \")\n",
        "    if nome.lower() == 'fim':\n",
        "        break\n",
        "    convidados.append(nome)\n",
        "\n",
        "# Lista para armazenar convidados que confirmaram\n",
        "confirmados = []\n",
        "\n",
        "# Adiciona confirmados\n",
        "while True:\n",
        "    nome = input(\"Quem confirmou? (ou digite 'fim' para encerrar) \")\n",
        "    if nome.lower() == 'fim':\n",
        "        break\n",
        "    confirmados.append(nome)\n",
        "\n",
        "# Identifica convidados que não confirmaram\n",
        "nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]\n",
        "\n",
        "# Exibe convidados que não confirmaram\n",
        "print(\"Convidados que ainda não confirmaram:\")\n",
        "for pessoa in nao_confirmados:\n",
        "    print(pessoa)\n",
        "\n",
        "# Mensagem final\n",
        "print(\"\\nEnviar lembretes para os convidados que não confirmaram.\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kfJQkHoYpnZ5",
        "outputId": "32796ebf-6de7-4c0f-fb0c-9b95e1af9f2e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quem você quer convidar? (ou digite 'fim' para encerrar) andre, bruno, thiago e elvis, fim\n",
            "Quem você quer convidar? (ou digite 'fim' para encerrar) fim\n",
            "Quem confirmou? (ou digite 'fim' para encerrar) andre\n",
            "Quem confirmou? (ou digite 'fim' para encerrar) bruno\n",
            "Quem confirmou? (ou digite 'fim' para encerrar) fim\n",
            "Convidados que ainda não confirmaram:\n",
            "andre, bruno, thiago e elvis, fim\n",
            "\n",
            "Enviar lembretes para os convidados que não confirmaram.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "meu_conjunto = set()\n",
        "\n",
        "#Add elementos do conjunto\n",
        "meu_conjunto.add(10)\n",
        "meu_conjunto.add(30)\n",
        "meu_conjunto.add(20)\n",
        "print(\"Os valores do meu conjunto eh\", meu_conjunto)\n",
        "#verificando se um elemento está no conjunto\n",
        "elemento = 30\n",
        "if elemento in meu_conjunto:\n",
        "    print(f\"{elemento} está no conjunto.\")\n",
        "else:\n",
        "    print(f\"{elemento} Não está no conjunto\")\n",
        "#Removendo um elemento do conjunto\n",
        "meu_conjunto.remove(30)\n",
        "print(\"Conjunto após o emento 30 ser removido\", meu_conjunto)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d-k8no8SnzOM",
        "outputId": "fe20d02d-b042-41a5-acb4-20f1607f017f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Os valores do meu conjunto eh {10, 20, 30}\n",
            "30 está no conjunto.\n",
            "Conjunto após o emento 30 ser removido {10, 20}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# importe da biblioteca NUMpy\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "my_array = np.array([1, 2, 3, 4, 5])\n",
        "print(\"Array original\",my_array)\n",
        "#Realizar operações matematicas com array\n",
        "squared_array = my_array ** 2 #Estou elevando ao quadrado\n",
        "sum_of_elements = np.sum(my_array) # calcula a soma de todos os elementos\n",
        "print(\"\\Array ao quadrado é:\")\n",
        "print(squared_array)\n",
        "print(\"\\nA Soma de todos os numeros é: \")\n",
        "print(sum_of_elements)\n",
        "element_at_index_2 = my_array[2]\n",
        "print(\"\\nElemento no indice 2:\", element_at_index_2)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TDxq_Y-cpiie",
        "outputId": "dadd65a5-c215-402c-8441-c6408104434a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Array original [1 2 3 4 5]\n",
            "\\Array ao quadrado é:\n",
            "[ 1  4  9 16 25]\n",
            "\n",
            "A Soma de todos os numeros é: \n",
            "15\n",
            "\n",
            "Elemento no indice 2: 3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Importe as bibliotecas necessárias\n",
        "\n",
        "import numpy as np\n",
        "\n",
        "# Dados dos participantes\n",
        "\n",
        "participantes = [\n",
        "\n",
        "    {   \"nome\": \"Alice\",\n",
        "\n",
        "        \"localizacao\": \"EUA\",\n",
        "\n",
        "        \"afiliacao\": \"Universidade A\",\n",
        "\n",
        "        \"interesses\": [\"Física\", \"Astronomia\"]\n",
        "\n",
        "    },\n",
        "\n",
        "    {\n",
        "\n",
        "        \"nome\": \"Bob\",\n",
        "\n",
        "        \"localizacao\": \"Brasil\",\n",
        "\n",
        "        \"afiliacao\": \"Instituto B\",\n",
        "\n",
        "        \"interesses\": [\"Biologia\", \"Astronomia\"]\n",
        "\n",
        "    },\n",
        "\n",
        "    {\n",
        "\n",
        "        \"nome\": \"Charlie\",\n",
        "\n",
        "        \"localizacao\": \"Índia\",\n",
        "\n",
        "        \"afiliacao\": \"Instituto C\",\n",
        "\n",
        "        \"interesses\": [\"Química\", \"Engenharia\"]\n",
        "\n",
        "    }\n",
        "\n",
        "    # Adicione mais participantes conforme necessário\n",
        "\n",
        "]\n",
        "\n",
        "# Usando sets para identificar diferentes regiões dos participantes\n",
        "\n",
        "regioes = set(participante[\"localizacao\"] for participante in participantes)\n",
        "\n",
        "# Usando um dicionário para categorizar afiliações\n",
        "\n",
        "afiliacoes = {}\n",
        "\n",
        "for participante in participantes:\n",
        "\n",
        "    afiliacao = participante[\"afiliacao\"]\n",
        "\n",
        "    if afiliacao not in afiliacoes:\n",
        "\n",
        "        afiliacoes[afiliacao] = []\n",
        "\n",
        "    afiliacoes[afiliacao].append(participante[\"nome\"])\n",
        "\n",
        "# Usando NumPy para analisar áreas de interesse\n",
        "\n",
        "areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante[\"interesses\"]])\n",
        "\n",
        "interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)\n",
        "\n",
        "area_mais_popular = interesses_unicos[np.argmax(contagem)]\n",
        "\n",
        "# Resultados\n",
        "\n",
        "print(\"Regiões dos participantes:\", regioes)\n",
        "\n",
        "print(\"Afiliações dos participantes:\")\n",
        "\n",
        "for afiliacao, nomes in afiliacoes.items():\n",
        "\n",
        "    print(f\"{afiliacao}: {', '.join(nomes)}\")\n",
        "\n",
        "print(\"Área de interesse mais popular:\", area_mais_popular)\n",
        "\n",
        "#Resultado:"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SnXWCsVFwaNc",
        "outputId": "29910528-ab83-4b06-958f-d151155c052c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Regiões dos participantes: {'Índia', 'Brasil', 'EUA'}\n",
            "Afiliações dos participantes:\n",
            "Universidade A: Alice\n",
            "Instituto B: Bob\n",
            "Instituto C: Charlie\n",
            "Área de interesse mais popular: Astronomia\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#fazendo classe com herança\n",
        "#Def e __int__ são contrutores de classe\n",
        "class Animal:\n",
        "    def __init__(self, nome):\n",
        "        self.nome = nome\n",
        "\n",
        "    def fazer_barulho(self):\n",
        "        pass\n",
        "class Homem(Animal):\n",
        "    def fazer_barulho(self):\n",
        "        return \"Te amo Tay\"\n",
        "class Mulher(Animal):\n",
        "    def fazer_barulho(self):\n",
        "        return \"Te amo mowzi\"\n",
        "Andre = Homem(\"Andre\")\n",
        "Taisla = Mulher(\"Taisla\")\n",
        "print(f\"{Andre.nome} diz: {Andre.fazer_barulho()}\")\n",
        "print(f\"{Taisla.nome} diz: {Taisla.fazer_barulho()}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "d-SyK1llzEr_",
        "outputId": "3138c380-0fd6-45b0-960d-2aa1d0d1cf7a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Andre diz: Te amo Tay\n",
            "Taisla diz: Te amo mowzi\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "math.sqrt(25)\n",
        "math.log2(1024)\n",
        "math.cos(45)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nTqT0hmX49qv",
        "outputId": "9fac16f0-12b8-4a33-d1ad-fad16d39cbe5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.5253219888177297"
            ]
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "# Raiz quadrada de 64\n",
        "print(\"Raiz quadrada de 25:\", math.sqrt(25))\n",
        "\n",
        "# Logaritmo base 2 de 1024\n",
        "print(\"Logaritmo base 2 de 1024:\", math.log2(1024))\n",
        "\n",
        "# Seno de 90 graus (convertendo de graus para radianos)\n",
        "print(\"seno de 90 graus:\", math.sin(math.radians(90)))\n",
        "\n",
        "# Cosseno de 90 graus (convertendo de graus para radianos)\n",
        "print(\"Cosseno de 90 graus:\", math.cos(math.radians(90)))\n",
        "\n",
        "# Tangente de 45 graus\n",
        "print(\"Tangente de 45 graus:\", math.tan(math.radians(45)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5kAa7Sxs5fD0",
        "outputId": "c336344a-54b2-4e8e-f6ff-8f4525d6025e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Raiz quadrada de 25: 5.0\n",
            "Logaritmo base 2 de 1024: 10.0\n",
            "seno de 90 graus: 1.0\n",
            "Cosseno de 90 graus: 6.123233995736766e-17\n",
            "Tangente de 45 graus: 0.9999999999999999\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "ang = int(input('Ângulo a ser calculado: '))\n",
        "rad = math.radians(ang)\n",
        "raiz = int(input('Número da raiz quadrada que deseja: '))\n",
        "log = int(input('Número para logaritmo: '))\n",
        "seno = math.sin(rad)\n",
        "cosseno = math.cos(rad)\n",
        "tangente = math.tan(rad)\n",
        "print(f'Seno: {seno:.2f}')\n",
        "print(f'Cosseno: {cosseno:.2f}')\n",
        "print(f'Tangente: {tangente:.2f}')\n",
        "print(f'Raiz quadrada: {math.sqrt(raiz):.2f}')\n",
        "print(f'Logaritmo: {math.log2(log):.2f}')\n"
      ],
      "metadata": {
        "id": "LUX3ct4q7dOI",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "aed011a6-d7f3-4eb6-a43c-e0fbcfc00650"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ângulo a ser calculado: 45\n",
            "Número da raiz quadrada que deseja: 121\n",
            "Número para logaritmo: 1024\n",
            "Seno: 0.71\n",
            "Cosseno: 0.71\n",
            "Tangente: 1.00\n",
            "Raiz quadrada: 11.00\n",
            "Logaritmo: 10.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Criando uma página HTML usando Python\n",
        "\n",
        "html_code = \"\"\"\n",
        "\n",
        "<!DOCTYPE html>\n",
        "\n",
        "<html>\n",
        "\n",
        "<head>\n",
        "\n",
        "  <title>Exemplo de Front-end com Python</title>\n",
        "\n",
        "</head>\n",
        "\n",
        "<body>\n",
        "\n",
        "  <h1>José gay!</h1>\n",
        "\n",
        "  <p>Policia viado.</p>\n",
        "\n",
        "</body>\n",
        "\n",
        "</html>\n",
        "\"\"\"\n",
        "from IPython.display import HTML\n",
        "\n",
        "HTML(html_code)\n"
      ],
      "metadata": {
        "id": "OyBxfPDH_ZM2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 100
        },
        "outputId": "254bf8d3-d07b-43e7-c36a-2b3849022ab3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "\n",
              "<!DOCTYPE html>\n",
              "\n",
              "<html>\n",
              "\n",
              "<head>\n",
              "\n",
              "  <title>Exemplo de Front-end com Python</title>\n",
              "\n",
              "</head>\n",
              "\n",
              "<body>\n",
              "\n",
              "  <h1>José gay!</h1>\n",
              "\n",
              "  <p>Policia viado.</p>\n",
              "\n",
              "</body>\n",
              "\n",
              "</html>\n"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Exemplo de HTML com botão usando Python\n",
        "from IPython.display import HTML\n",
        "html_code = \"\"\"\n",
        "\n",
        "<!DOCTYPE html>\n",
        "\n",
        "<html lang=\"en\">\n",
        "\n",
        "<head>\n",
        "\n",
        "    <meta charset=\"UTF-8\">\n",
        "\n",
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n",
        "\n",
        "    <title>Minha Primeira Página Web</title>\n",
        "\n",
        "    <style>\n",
        "\n",
        "        body {\n",
        "\n",
        "            font-family: 'Arial', sans-serif;\n",
        "\n",
        "            background-color: #f8f8f8;\n",
        "\n",
        "            margin: 0;\n",
        "\n",
        "            display: flex;\n",
        "\n",
        "            justify-content: center;\n",
        "\n",
        "            align-items: center;\n",
        "\n",
        "            height: 100vh;\n",
        "\n",
        "        }\n",
        "\n",
        "\n",
        "\n",
        "        .container {\n",
        "\n",
        "            text-align: center;\n",
        "\n",
        "            padding: 40px;\n",
        "\n",
        "            background-color: #fff;\n",
        "\n",
        "            border-radius: 8px;\n",
        "\n",
        "            box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);\n",
        "\n",
        "        }\n",
        "\n",
        "\n",
        "\n",
        "        h1 {\n",
        "\n",
        "            color: #3498db;\n",
        "\n",
        "            font-size: 2em;\n",
        "\n",
        "            margin-bottom: 20px;\n",
        "\n",
        "        }\n",
        "\n",
        "\n",
        "\n",
        "        p {\n",
        "\n",
        "            color: #555;\n",
        "\n",
        "            font-size: 1.2em;\n",
        "\n",
        "        }\n",
        "\n",
        "\n",
        "\n",
        "        button {\n",
        "\n",
        "            background-color: #3498db;\n",
        "\n",
        "            color: #fff;\n",
        "\n",
        "            font-size: 1.2em;\n",
        "\n",
        "            padding: 10px 20px;\n",
        "\n",
        "            border: none;\n",
        "\n",
        "            border-radius: 4px;\n",
        "\n",
        "            cursor: pointer;\n",
        "\n",
        "            transition: background-color 0.3s ease;\n",
        "\n",
        "        }\n",
        "\n",
        "\n",
        "\n",
        "        button:hover {\n",
        "\n",
        "            background-color: #2980b9;\n",
        "\n",
        "        }\n",
        "\n",
        "    </style>\n",
        "\n",
        "</head>\n",
        "\n",
        "<body>\n",
        "\n",
        "    <div class=\"container\">\n",
        "\n",
        "        <h1>Olá, Mundo!</h1>\n",
        "\n",
        "        <p>Esta é minha primeira página web criada com Python no Colab. Bem-vindo ao mundo da programação web!</p>\n",
        "\n",
        "        <button onclick=\"alert('Botão clicado!')\">Clique em Mim</button>\n",
        "\n",
        "    </div>\n",
        "\n",
        "</body>\n",
        "\n",
        "</html>\n",
        "\"\"\"\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "# Exibindo a página HTML\n",
        "\n",
        "from IPython.display import HTML\n",
        "\n",
        "HTML(html_code)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "WeWvEV-R1FGg",
        "outputId": "3f4fdbca-9e54-407e-d781-7f31607196b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "\n",
              "<!DOCTYPE html>\n",
              "\n",
              "<html lang=\"en\">\n",
              "\n",
              "<head>\n",
              "\n",
              "    <meta charset=\"UTF-8\">\n",
              "\n",
              "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n",
              "\n",
              "    <title>Minha Primeira Página Web</title>\n",
              "\n",
              "    <style>\n",
              "\n",
              "        body {\n",
              "\n",
              "            font-family: 'Arial', sans-serif;\n",
              "\n",
              "            background-color: #f8f8f8;\n",
              "\n",
              "            margin: 0;\n",
              "\n",
              "            display: flex;\n",
              "\n",
              "            justify-content: center;\n",
              "\n",
              "            align-items: center;\n",
              "\n",
              "            height: 100vh;\n",
              "\n",
              "        }\n",
              "\n",
              "\n",
              "\n",
              "        .container {\n",
              "\n",
              "            text-align: center;\n",
              "\n",
              "            padding: 40px;\n",
              "\n",
              "            background-color: #fff;\n",
              "\n",
              "            border-radius: 8px;\n",
              "\n",
              "            box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);\n",
              "\n",
              "        }\n",
              "\n",
              "\n",
              "\n",
              "        h1 {\n",
              "\n",
              "            color: #3498db;\n",
              "\n",
              "            font-size: 2em;\n",
              "\n",
              "            margin-bottom: 20px;\n",
              "\n",
              "        }\n",
              "\n",
              "\n",
              "\n",
              "        p {\n",
              "\n",
              "            color: #555;\n",
              "\n",
              "            font-size: 1.2em;\n",
              "\n",
              "        }\n",
              "\n",
              "\n",
              "\n",
              "        button {\n",
              "\n",
              "            background-color: #3498db;\n",
              "\n",
              "            color: #fff;\n",
              "\n",
              "            font-size: 1.2em;\n",
              "\n",
              "            padding: 10px 20px;\n",
              "\n",
              "            border: none;\n",
              "\n",
              "            border-radius: 4px;\n",
              "\n",
              "            cursor: pointer;\n",
              "\n",
              "            transition: background-color 0.3s ease;\n",
              "\n",
              "        }\n",
              "\n",
              "\n",
              "\n",
              "        button:hover {\n",
              "\n",
              "            background-color: #2980b9;\n",
              "\n",
              "        }\n",
              "\n",
              "    </style>\n",
              "\n",
              "</head>\n",
              "\n",
              "<body>\n",
              "\n",
              "    <div class=\"container\">\n",
              "\n",
              "        <h1>Olá, Mundo!</h1>\n",
              "\n",
              "        <p>Esta é minha primeira página web criada com Python no Colab. Bem-vindo ao mundo da programação web!</p>\n",
              "\n",
              "        <button onclick=\"alert('Botão clicado!')\">Clique em Mim</button>\n",
              "\n",
              "    </div>\n",
              "\n",
              "</body>\n",
              "\n",
              "</html>\n"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from IPython.display import HTML\n",
        "\n",
        "html_code = \"\"\"\n",
        "\n",
        "<!DOCTYPE html>\n",
        "\n",
        "<html lang=\"en\">\n",
        "\n",
        "<head>\n",
        "\n",
        "    <meta charset=\"UTF-8\">\n",
        "\n",
        "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n",
        "\n",
        "    <title>Meu Perfil</title>\n",
        "\n",
        "</head>\n",
        "\n",
        " <body style=\"font-family: 'Arial', sans-serif; background-color: #e0e0e0; margin: 0; padding: 0;\">\n",
        "\n",
        "\n",
        "\n",
        "    <header style=\"text-align: center; background-color: #e74c3c; color: #fff; padding: 20px;\">\n",
        "\n",
        "\n",
        "        <h1 style=\"margin: 0;\">André Luis Cruz Lima de Oliveira</h1>\n",
        "\n",
        "        <p style=\"margin: 5px 0;\">Desenvolvedor Web</p>\n",
        "\n",
        "    </header>\n",
        "\n",
        "\n",
        "\n",
        "    <section style=\"margin: 20px; text-align: center;\">\n",
        "\n",
        "        <img src=\"https://imgur.com/9zaUDeW.png\" alt=\"Descrição da Imagem\" style=\"border-radius: 50%; margin-bottom: 20px;\">\n",
        "\n",
        "        <div id=\"informacoes-pessoais\" style=\"max-width: 400px; margin: 0 auto;\">\n",
        "\n",
        "            <p>Cidade: Salvador </p>\n",
        "\n",
        "            <p>País: Brasil</p>\n",
        "\n",
        "            <p>Interesses: Web Development, Programação, Redes.</p>\n",
        "\n",
        "        </div>\n",
        "\n",
        "    </section>\n",
        "\n",
        "\n",
        "\n",
        "    <section style=\"margin: 20px; text-align: center;\">\n",
        "\n",
        "        <h2>Habilidades</h2>\n",
        "\n",
        "        <ul style=\"list-style: none; padding: 0;\">\n",
        "\n",
        "            <li>Linguagens: Python, HTML, Redes</li>\n",
        "\n",
        "            <li>Ferramentas: Git, VS Code, Collab</li>\n",
        "\n",
        "        </ul>\n",
        "\n",
        "    </section>\n",
        "\n",
        "\n",
        "\n",
        "    <section style=\"margin: 20px; text-align: center;\">\n",
        "\n",
        "        <h2>Projeto Recente</h2>\n",
        "\n",
        "        <p>Trabalhando em um site pessoal para mostrar meu portfólio.</p>\n",
        "\n",
        "    </section>\n",
        "\n",
        "\n",
        "\n",
        "    <footer style=\"text-align: center; margin-top: 20px;\">\n",
        "\n",
        "        <a href=\"https://www.linkedin.com/in/andr%C3%A9-luis-cruz-lima-de-oliveira-682560318/\" target=\"_blank\" style=\"margin: 0 10px; color: #3498db; text-decoration: none;\">LinkedIn</a>\n",
        "\n",
        "    </footer>\n",
        "\n",
        "</body>\n",
        "\n",
        "</html>\n",
        "\"\"\"\n",
        "\n",
        "\n",
        "# Exibindo a página HTML\n",
        "\n",
        "HTML(html_code)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 627
        },
        "id": "3RttePImcvRR",
        "outputId": "65568de9-8567-4e98-e85f-581f4b52ba1b"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "\n",
              "<!DOCTYPE html>\n",
              "\n",
              "<html lang=\"en\">\n",
              "\n",
              "<head>\n",
              "\n",
              "    <meta charset=\"UTF-8\">\n",
              "\n",
              "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n",
              "\n",
              "    <title>Meu Perfil</title>\n",
              "\n",
              "</head>\n",
              "\n",
              " <body style=\"font-family: 'Arial', sans-serif; background-color: #e0e0e0; margin: 0; padding: 0;\">\n",
              "\n",
              "\n",
              "\n",
              "    <header style=\"text-align: center; background-color: #e74c3c; color: #fff; padding: 20px;\">\n",
              "\n",
              "\n",
              "        <h1 style=\"margin: 0;\">André Luis Cruz Lima de Oliveira</h1>\n",
              "\n",
              "        <p style=\"margin: 5px 0;\">Desenvolvedor Web</p>\n",
              "\n",
              "    </header>\n",
              "\n",
              "\n",
              "\n",
              "    <section style=\"margin: 20px; text-align: center;\">\n",
              "\n",
              "        <img src=\"https://imgur.com/9zaUDeW.png\" alt=\"Descrição da Imagem\" style=\"border-radius: 50%; margin-bottom: 20px;\">\n",
              "\n",
              "        <div id=\"informacoes-pessoais\" style=\"max-width: 400px; margin: 0 auto;\">\n",
              "\n",
              "            <p>Cidade: Salvador </p>\n",
              "\n",
              "            <p>País: Brasil</p>\n",
              "\n",
              "            <p>Interesses: Web Development, Programação, Redes.</p>\n",
              "\n",
              "        </div>\n",
              "\n",
              "    </section>\n",
              "\n",
              "\n",
              "\n",
              "    <section style=\"margin: 20px; text-align: center;\">\n",
              "\n",
              "        <h2>Habilidades</h2>\n",
              "\n",
              "        <ul style=\"list-style: none; padding: 0;\">\n",
              "\n",
              "            <li>Linguagens: Python, HTML, Redes</li>\n",
              "\n",
              "            <li>Ferramentas: Git, VS Code, Collab</li>\n",
              "\n",
              "        </ul>\n",
              "\n",
              "    </section>\n",
              "\n",
              "\n",
              "\n",
              "    <section style=\"margin: 20px; text-align: center;\">\n",
              "\n",
              "        <h2>Projeto Recente</h2>\n",
              "\n",
              "        <p>Trabalhando em um site pessoal para mostrar meu portfólio.</p>\n",
              "\n",
              "    </section>\n",
              "\n",
              "\n",
              "\n",
              "    <footer style=\"text-align: center; margin-top: 20px;\">\n",
              "\n",
              "        <a href=\"https://www.linkedin.com/in/andr%C3%A9-luis-cruz-lima-de-oliveira-682560318/\" target=\"_blank\" style=\"margin: 0 10px; color: #3498db; text-decoration: none;\">LinkedIn</a>\n",
              "\n",
              "    </footer>\n",
              "\n",
              "</body>\n",
              "\n",
              "</html>\n"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "qExe5jpKcKfu"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
