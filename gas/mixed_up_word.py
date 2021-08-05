from random import randint


def mixed_up_word(word):
    list_index_mixed_up = []
    while(len(list_index_mixed_up) < len(word)):
        index_random = randint(0, len(word)-1)
        if index_random not in list_index_mixed_up:
            list_index_mixed_up.append(index_random)
    word_random = ""
    print(list_index_mixed_up)
    for i in list_index_mixed_up:
        word_random = word_random + word[i]
    return word_random.lower()

print(mixed_up_word("Arthur"))