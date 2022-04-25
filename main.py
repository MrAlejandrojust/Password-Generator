import random


def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)


def main():
    upper_case_letter1 = chr(random.randint(65, 90))
    upper_case_letter2 = chr(random.randint(65, 90))
    lower_case_letter1 = chr(random.randint(97, 122))
    lower_case_letter2 = chr(random.randint(97, 122))
    digit1 = str(random.randint(0, 9))
    digit2 = str(random.randint(0, 9))
    punctuation_sign1 = chr(random.randint(33, 152))
    punctuation_sign2 = chr(random.randint(33, 152))

    password = shuffle(upper_case_letter1 + upper_case_letter2 + lower_case_letter1 + lower_case_letter2 + digit1 +
                       digit2 + punctuation_sign1 + punctuation_sign2)

    print(password)


if __name__ == '__main__':
    main()
