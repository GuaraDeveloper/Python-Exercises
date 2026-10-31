# Exercício 2: pares sem repetição
# Pega os números pares de uma lista, tira os repetidos e mostra em ordem crescente

entrada = [4, 7, 2, 5, 9, 10, 2, 6]
pares = []

for numero in entrada:
    # só guarda se for par e ainda não estiver na lista de pares
    if numero % 2 == 0 and numero not in pares:
        pares.append(numero)

pares.sort()  # coloca a lista em ordem crescente

print("Saída =", pares)
