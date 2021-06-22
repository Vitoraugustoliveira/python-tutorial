# Lists

list1 = []
print(type(list1))

lista = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]

matrix = [lista, lista2]
print(matrix)
print(matrix[0][1])

soma_lista = lista + lista2
print(soma_lista)

lista.append(85)
print(lista)
print(lista[-5])
print(lista[0])

lista.append("XABLAU")
print(lista)

lista.append(lista2)
print(lista)

print(lista.index("XABLAU"))

del lista[lista.index("XABLAU")]
del lista[0]
lista.pop()
print(lista)

#lista = [1, 2, 3, 4]
# pos - -> value
# 0 - -> 1
# 1 - -> 2
# 2 - -> 3
# 3 - -> 4
# -1 - -> 4
# -2 - -> 3
# -3 - -> 2
# -4 - -> 1

# Dict

# Tuples

# Sets
