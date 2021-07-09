""" def hello_world():
    print("hello_world")
    hello_world()

hello_world()
 """

# iterativa
def fatorial(n):
    for i in range(n-1, 1, -1):
        n = n*i
    return n

#print(fatorial(3))

# de forma recursiva
def fatorial_recursivo(n):
    if n <= 1:
        return n
    else:
        return n * fatorial_recursivo(n-1)
""" 
5 = 120
5*24
4*6
3*2
2*1
1 """

print(fatorial_recursivo(10))