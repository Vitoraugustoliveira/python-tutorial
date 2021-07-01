# naturais -> 0, 1,2,3,4,5,6,7
# inteiros -> -1, -2, 0, 1
# reais -> 1.4

# int(4) --> 4
# float(4) --> 4.0


# 4 laranjas
# 2 maças


# joao

# 7 limoes
# 1 maça


arthur = {"laranjas", "limoes", "laranjas"}
print(arthur)
print(type(arthur))
arthur.remove("laranjas")
arthur.discard("batata")
print(arthur)

lista = [1,2,3,2,2,2,5,6, "limoes"]
print(list(set(lista)))

#union_arthur_lista = arthur.union(set(lista))
union_arthur_lista = arthur | set(lista)
print(union_arthur_lista)

print("limoes" in union_arthur_lista)

conjunto1 = {1,2,3} #conjunto1 é subconjunto de conjunto2
conjunto2 = {1,2,3,4,5,6}

conjunto3 = {25,4,3}

print(conjunto1 <= conjunto2) #verificar se conjunto 1 é subconjunto de 2

print(conjunto1 & conjunto2) #interseção entre conjuntos
print(conjunto3 & conjunto2) #interseção entre conjuntos

print(conjunto2 - conjunto1) #diferença entre conjuntos