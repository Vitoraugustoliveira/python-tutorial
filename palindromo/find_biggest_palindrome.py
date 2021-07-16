# criar a função que testa se uma string é palindromo - check
# crio uma função para ir obtendo todas as substrings possíveis da string inicial
# substring que é o maior palíndromo

def validate_palindrome(word):
    for i in range(0, int(len(word)/2)):
        if word[i] != word[-1-i]:
            return False
        continue
    return True


""" print("retorna de espaço vazio", validate_palindrome(""))

print("Teste banana", validate_palindrome("banana"))
print("Teste anana", validate_palindrome("anana"))
print("Teste ana", validate_palindrome("anana"))
 """


def get_substring(word, type_):
    if type_ == "first":
        return word[1:]
    if type_ == "last":
        return word[:-1]
    if type_ == "both":
        return word[1:-1]


array_type = ["first", "last", "both"]


def get_biggest_palindrome(word):
    aux = ""
    while True:
        if validate_palindrome(word):
            return word
        for type_ in array_type:
            aux = get_substring(word, type_)
            if validate_palindrome(aux):
                return aux
            if type_ == "both":
                word = aux[:]
            aux = word[:]
            continue


word = "million"
print(get_biggest_palindrome(word))
