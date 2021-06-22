""" Calculate IMC """

# comments
# count = 1
# while True:
#   print(count)
#   count = count + 1
#   if (count == 25):
#     break


while True:
    try:
        weight = float(input("Digite o seu peso em kilogramas\n"))
        if 1.5 < weight < 250:
            print("Você digitou um valor possível para peso!")
            break
        print("Você digitou um valor impossível para um peso humano")
    except ValueError as err:
        print(err)
        print("Você digitou uma string")
        continue

height = float(input("Digite a sua altura em metros\n"))

imc = weight/(height**2)

print("Seu imc é: ", imc)

if imc < 18.5:
    print("Magro demais")
elif 18.5 <= imc <= 24.9:
    print("Peso normal")
elif 24.9 < imc <= 29.9:
    print("Sobrepeso")
elif 29.9 < imc <= 34.9:
    print("Obesidade Severa")
elif 34.9 < imc <= 39.9:
    print("Sobrepeso")
else:
    print("Tá gordo")
