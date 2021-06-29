number = int(input("Digite um numero para validar se ele é primo\n"))

primo = True
for i in range(1, number+1):
	if i == 1 or i == number:
		continue
	if number%i == 0:
		print("Número {} não é primo".format(number))
		primo = False
		break

if primo == True:
	print("Número {} é primo".format(number))