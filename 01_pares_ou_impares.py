# Exercício 1: pares ou ímpares
# Mostra os números pares ou ímpares de uma lista, sem repetição e em ordem crescente

entrada = [4, 7, 2, 4, 9, 10, 2, 6]

pares = []
impares = []

# percorre a lista e separa os números, sem guardar repetidos
for numero in entrada:
    # número % 2 == 0 significa que o resto da divisão por 2 é zero (número par)
    if numero % 2 == 0 and numero not in pares:
        pares.append(numero)
    elif numero % 2 != 0 and numero not in impares:
        impares.append(numero)

# deixa as duas listas em ordem crescente
pares.sort()
impares.sort()

# strip() tira espaços e lower() deixa em minúsculas, assim "Pares " também funciona
escolha = input("Números pares ou ímpares? ").strip().lower()

if escolha == "pares":
    print("Seus números são:", pares)
elif escolha in ("impares", "ímpares"):
    print("Seus números são:", impares)
else:
    print("Responda somente 'pares' ou 'ímpares'.")
