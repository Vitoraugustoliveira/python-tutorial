key_value = {}

key_value = {"Maria": 8, "Joao": 1, "Vitor": 9}
print(key_value)
print(type(key_value))

print(key_value["Maria"])

print(key_value.get("Maraia", "QUALUER_COISA"))


# key_value.items()
# key_value.values()
# key_value.keys()

for key,value in key_value.items():
	print("{}:{}".format(key,value), end=", ")

print("\n")
for value in key_value.values():
	print("Valor é ", value)


for key in key_value.keys():
	print("Chave é ", key)


lista_de_valores_do_dict = list(key_value.values())
print(lista_de_valores_do_dict)

#outra forma de definir dict
dictionary = dict(a=1,b=2,c=3)
print(dictionary)

dictionary.update({"d": 4, "e": 5}) #forma de atualizar dict
print(dictionary)

print("*"*80)
print("TUPLAS")
print("*"*80)

## TUPLAS

#Tuplas são como listas, mas são IMUTÁVEIS, uma vez atribuído o valor para elas, não se pode, não se é permitido, altera-lo

tupla = (1,2,3,4)
print(tupla)
print(type(tupla))

# tupla[0] = 3 # como tupla é imutavel, essa linha de código dá pau, lança exceção

outra_tupla = tuple([1,2,3,4,5])
print(outra_tupla)

result = divmod(7,3) # divmod retorna tupla com o valor da divisão, no caso 7/3 = 2 e com o valor do resto da divisão, no caso 1
print(result)

quociente, resto = result
print(quociente)
print(resto)

bla, xa = [2,3]
print(bla)
print(xa)