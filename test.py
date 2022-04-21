# import

def test():

    fhand = input('Please enter file path: ')
    try:
        fhand = open(fhand)
    except:
        print('File has not been found in path.')
        quit()

    words_dict = dict()
    for letter in fhand:
        words = letter.rstrip().split()
        for word in words:
            words_dict[word] = words_dict.get(word, 0) + 1

    words_list = list()
    for k, v in words_dict.items():
        newtup = (k, v)
        words_list.append(newtup)

    words_list = sorted(words_list, reverse=True)

    for k, v in words_list[:10]:
        print(k, v)


if __name__ == '__main__':
    test()
