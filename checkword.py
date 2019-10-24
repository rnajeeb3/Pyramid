# parse given word
def check_word(word):
    list_word = list(word)
    word_dict = dict.fromkeys(list_word, 0)

    # make dictionary of letters and number of occurrences
    for l in list_word:
        word_dict[l] = word_dict[l] + 1
    print(word_dict)

    # list of occurrences
    values = list(word_dict.values())
    values.sort()

    # compare list of pyramid word occurrences with given word
    if values[0] == 1:
        rlist = list(range(1, (len(values) + 1)))
        print(rlist)
        if rlist == values:
            return True
        else:
            return False
    else:
        return False


