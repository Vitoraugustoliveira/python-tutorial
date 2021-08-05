""" Module Gas """

""" Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. """

def get_price_total(litres: float, fuel_type: str) -> float:
    base_price_gas = 2.5
    base_price_alcohol = 1.9
    if litres <= 20:
        if fuel_type == "A":
            return litres*(base_price_alcohol*(100-3)/100)
        elif fuel_type == "G":
            return litres*(base_price_gas*(100-4)/100)
        else:
            print("Fuel Type doesn't exists!")
            return -1
    else:
        if fuel_type == "A":
            return (litres*(base_price_alcohol)*(100-5)/100)
        elif fuel_type == "G":
            return (litres*(base_price_gas)*(100-6)/100)
        else:
            print("Fuel Type doesn't exists!")
            return -1


price = get_price_total(20, "A")
if price == -1:
    print("deu ruim")
else:
    print(price)

def get_litres_total(price: float, fuel_type: str, discount) -> float:
    base_price_gas = 2.5
    base_price_alcohol = 1.9
    if fuel_type == "A":
        litres = price/(base_price_alcohol*discount)
    elif fuel_type == "G":
        litres = price/(base_price_gas*discount)
    else:
        print("Fuel type doesn't exists!")
        litres = -1
    return litres

litres = get_litres_total(36.85999999999999, "A", 0.95)
print(litres)