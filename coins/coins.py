from random import randint
import matplotlib.pyplot as plt

""" y = [quantidade de vezes que lancei as 4 moedas]
x = [probabilidade]

qnt de vezes --> probabilidade
10 --> probabilidade
20 --> probabilidade
30 --> probabilidade """

quantidade_de_lancamentos = [10,20,30,40,50,60,70,80,90,100, 150, 200, 250, 300, 350, 400,450, 500, 1000, 2000, 3000, 5000, 10000, 20000, 50000, 100000]

probabilidades = []
# esse bloco termina aonde? Termina no result_final = []
# esse bloco é o for mais externo, onde ele termina? Quando a identação voltar para o mesmo alinhamento dele
for qnt_lanc in quantidade_de_lancamentos:
    result_final = []
    # e esse bloco?
    for n in range(0, qnt_lanc):
        result = []
        for i in range(0,4):
            result.append(randint(1,2)) # de 1 a 2, pega numero aleatorio de 1 a 2, se fosse randint(1,10), seria de 1 a 10
        result_final.append(result)
    probabilidades.append(sum([1 for i in result_final if (i.count(1) == 4 and i.count(2) == 2)])/qnt_lanc)
    result_final = []


print(probabilidades)
print(len(probabilidades))

plt.plot(quantidade_de_lancamentos, probabilidades)
plt.ylabel("Quantidade de lançamentos")
plt.xlabel("probabilidades")
plt.show()