# Exercício 3: números primos em um intervalo
# Mostra todos os números primos entre início e fim (inclusive)
# Um número primo só é divisível por 1 e por ele mesmo

inicio = 10
fim = 20

primos = []

for numero in range(inicio, fim + 1):
    # números menores ou iguais a 1 não são primos
    if numero > 1:
        # testa se algum número entre 2 e (numero - 1) divide o número sem resto
        for i in range(2, numero):
            if numero % i == 0:
                break  # achou um divisor: não é primo, para de testar
        else:
            # o else do for só roda se o for terminou SEM break,
            # ou seja, nenhum divisor foi encontrado: o número é primo
            primos.append(numero)

print("Saída =", primos)
