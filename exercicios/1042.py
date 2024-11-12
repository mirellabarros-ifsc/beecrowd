entrada = input().split()
lista = list(map(int, entrada))

lista_ordenada = lista.copy()
lista_ordenada.sort()

for i in range(len(lista_ordenada)):
    print(lista_ordenada[i])

print()

for i in range(len(lista)):
    print(lista[i])


