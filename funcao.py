def print_1_to_10():
	for i in range(1, 11):
		print(i)


def remove_duplicated(lista):
	lista_without_duplicated = list(set(lista))
	return lista_without_duplicated

print_1_to_10()
print_1_to_10()
print_1_to_10()
print_1_to_10()

print(remove_duplicated())