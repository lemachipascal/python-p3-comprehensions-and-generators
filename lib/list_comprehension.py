def return_evens(num_list):
    evens = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
    return evens

def make_exclamation(sentence_list):
    make = []
    for sentence in sentence_list:
        make.append(sentence + '!')
    return make