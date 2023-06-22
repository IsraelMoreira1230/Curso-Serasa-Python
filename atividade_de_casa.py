lista = [13, -3, 5, 9, 19, 46, 79, 37, -18, 3, 13, 7, 4, 4, -42]

# Imprimir o maior elemento
maior = max(lista)
print("Maior elemento:", maior)

# Imprimir o menor elemento
menor = min(lista)
print("Menor elemento:", menor)

# Imprimir os números pares
pares = [numero for numero in lista if numero % 2 == 0]
print("Números pares:", pares)

# Imprimir o número de ocorrências do primeiro elemento da lista
primeiro_elemento = lista[0]
ocorrencias = lista.count(primeiro_elemento)
print("Número de ocorrências do primeiro elemento:", ocorrencias)

# Imprimir a média dos elementos
media = sum(lista) / len(lista)
print("Média dos elementos:", media)

# Imprimir a soma dos elementos de valor negativo
soma_negativos = sum(numero for numero in lista if numero < 0)
print("Soma dos elementos de valor negativo:", soma_negativos)
