import sys
import time
import os


def power2(n):
    # n = int(input('Enter a number: '))
    n = n

    if n > 0 and (n & n - 1) == 1:
        print('Is power of 2')
    else:
        print("Isn't power of 2")


def mult(a, b):
    a = int(a)
    b = int(b)
    product = 0

    for c in range(1, b + 1, 1):
        product = product + a

    print(f'Result: {product}')


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()
    return value


def clearScreen():
    os.system("cls")


def test():
    fhand = input('Please enter file path: ')
    try:
        fhand = open(fhand)
    except SyntaxError:
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
