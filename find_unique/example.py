"""
Faça um programa que peça o tamanho de um arquivo
para download (em MB) e a velocidade de um link de 
Internet (em Mbps), calcule e informe o
tempo aproximado de download do arquivo usando
este link (em minutos).
"""

def calculate_time(size_, speed_link):
    res = size_/speed_link
    return res


file_size = float(input("Digite o tamanho do arquivo\n"))
speed_link = float(input("Digite a velocidade da internet\n"))
print(calculate_time(file_size, speed_link))


""" 

    50 mb = x segundos
    50 mb = 1s

size = x
speed_link = 1

x = size/speed

x = 50 *1

50x = 50
x = 50/50 
x = 1
x =  """