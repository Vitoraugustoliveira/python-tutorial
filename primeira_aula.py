numero = 2

print(numero)
print(type(numero))


# quais os tipos básicos que existems?

"""
int
float
str --> string type
bool --> boolean type

"""

numero = 2.6
print(numero)
print(type(numero))

tipo_string = "a"

print(tipo_string)
print(type(tipo_string))

banana = "banana"

print(banana)
print(type(banana))

vdd = True
false = False

print(vdd)
print(type(vdd))


# OPERADORES
# soma
print(2+2.6)

# multiplicação
print(2*8)

# potencia
print(5**2)

print(5**(1/2))


# subtração

print(5-5)

# divisao
print(4/2)

print("banana" + str(numero))

print("ba" + "na"*2)

print("=============================================================")
print("="*80)


# operadores de comparação
compare_result = 2 == 3
print("2 == 3 ?", compare_result)

compare_result = 2 != 3
print("2 != 3 ?", compare_result)

print(bool(0))
print(bool(""))
print(bool(2))


qnt_orange = 10


if qnt_orange < 10:
    print("Valor final da compra não ganhou desconto")
else:
    print("Valor final aplicado com desconto de 80%")


value = input("Digite a quantidade de laranjas que você comprou:\n")
print(value)
print(type(value))


if int(value) < 10:
    print("Valor final da compra não ganhou desconto")
else:
    print("Valor final aplicado com desconto de 80%")
