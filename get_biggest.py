# numero1 = float(input("Digite o numero 1\n"))
# numero2 = float(input("Digite o numero 2\n"))
# numero3 = float(input("Digite o numero 3\n"))


numero1 = 40
numero2 = 30
numero3 = 50
lista_entrada = [numero1, numero2, numero3]
lista_entrada.sort()
print("O maior numero é: ", lista_entrada[-1])
print("O menor numero é: ", lista_entrada[0])


#imprimindo em ordem descrescente

lista= ["Z", "A", "T"]
lista.sort(reverse = True)
print(lista)

lista_entrada.sort(reverse = True)
for item in lista_entrada:
	print(item)


