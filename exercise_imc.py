weight = 70
height = 1.68


imc = weight/(height**2)

print(imc)


if imc < 18.5:
    print("Magro demais")
elif imc >= 18.5 and imc < 24.9:
    print("Peso normal")
else:
    print("Tá gordo")
