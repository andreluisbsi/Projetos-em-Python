# Lista para armazenar convidados
convidados = []

# Coletar convidados
while True:
    nome = input("Quem você quer convidar? (ou digite 'fim' para encerrar) ")
    if nome.lower() == 'fim':
        break
    convidados.append(nome)

# Listas para presença e ausência
presentes = []
ausentes = []

# Coletar confirmações
while True:
    nome = input("Quem está presente? (ou digite 'fim' para encerrar) ")
    if nome.lower() == 'fim':
        break
    if nome in convidados:
        presentes.append(nome)
    else:
        print(f"{nome} não está na lista de convidados.")

# Identificar ausentes
ausentes = [convidado for convidado in convidados if convidado not in presentes]

# Exibir resultados
print("\nConvidados presentes:")
for pessoa in presentes:
    print(f"- {pessoa}")

print("\nConvidados ausentes:")
for pessoa in ausentes:
    print(f"- {pessoa}")


Esse código implementa um sistema de lista de convidados em Python.

Primeiro o usuário cadastra os convidados.

Depois, informa quem está presente.

No final, o programa exibe quem compareceu e quem faltou.

1. Lista de convidados
convidados = []


Cria uma lista vazia onde serão armazenados os nomes dos convidados.

2. Coletar convidados
while True:
    nome = input("Quem você quer convidar? (ou digite 'fim' para encerrar) ")
    if nome.lower() == 'fim':
        break
    convidados.append(nome)


Loop infinito (while True).

input(...) pergunta ao usuário quem será convidado.

Se o usuário digitar "fim" (em qualquer combinação de maiúsculas/minúsculas, graças a lower()), o loop encerra.

Caso contrário, o nome é adicionado à lista convidados.

3. Listas para presença/ausência
presentes = []
ausentes = []


Inicializa duas listas:

presentes → convidados que confirmaram presença.

ausentes → convidados que não apareceram.

4. Coletar confirmações de presença
while True:
    nome = input("Quem está presente? (ou digite 'fim' para encerrar) ")
    if nome.lower() == 'fim':
        break
    if nome in convidados:
        presentes.append(nome)
    else:
        print(f"{nome} não está na lista de convidados.")


Outro loop infinito para registrar presença.

Pergunta ao usuário quem compareceu.

Se digitar "fim", o loop encerra.

Se o nome informado está na lista de convidados → é adicionado à lista presentes.

Caso contrário, mostra aviso: esse nome não estava na lista oficial de convidados.

5. Identificar ausentes
ausentes = [convidado for convidado in convidados if convidado not in presentes]


Cria uma nova lista ausentes usando list comprehension.

Percorre todos os nomes em convidados.

Adiciona à lista quem não está em presentes.

6. Exibir resultados
print("\nConvidados presentes:")
for pessoa in presentes:
    print(f"- {pessoa}")

print("\nConvidados ausentes:")
for pessoa in ausentes:
    print(f"- {pessoa}")


Imprime separadamente a lista de presentes e a de ausentes, cada nome em uma linha.
