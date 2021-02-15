#extended Euclidean algorithm
def extended_Euclidean_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        div, x, y = extended_Euclidean_algorithm(b % a, a)
    return (div, y - (b // a) * x, x)

#simple substitution encryptiom
def simple_substitution_encryptiom(text, key):
    dictionary = new_eng_dictionary()
    reverse_dictionary = new_eng_reverse_dictionary()
    power_dictionary = len(dictionary)
    #len of text and key
    len_text = len(text)
    len_key = len(key)
    #lower of text and key
    text_lower = text.lower()
    key_lower = key.lower()
    #lower of text and key => lower list of text and key
    text_lower_list = list(text_lower)
    key_lower_list = list(key_lower)
    wp = 0
    for items in range(len_key):
        wp = ((wp * dictionary[key_lower_list[items]]) + dictionary[key_lower_list[items]])
    wp = wp % power_dictionary
    for items in range(len_text):
        replacement = (dictionary[text_lower_list[items]] + wp) % power_dictionary
        text_lower_list.insert(items, reverse_dictionary[replacement])
        text_lower_list.pop(items + 1)       
    text = ''.join(text_lower_list)
    return text

#simple substitution encryptiom
def simple_substitution_decryptiom(text, key):
    dictionary = new_eng_dictionary()
    reverse_dictionary = new_eng_reverse_dictionary()
    power_dictionary = len(dictionary)
    #len of text and key
    len_text = len(text)
    len_key = len(key)
    #lower of text and key
    text_lower = text.lower()
    key_lower = key.lower()
    #lower of text and key => lower list of text and key
    text_lower_list = list(text_lower)
    key_lower_list = list(key_lower)
    wp = 0
    for items in range(len_key):
        wp = ((wp * dictionary[key_lower_list[items]]) + dictionary[key_lower_list[items]])
    wp = wp % power_dictionary
    for items in range(len_text):
        replacement = (dictionary[text_lower_list[items]] - wp) % power_dictionary
        text_lower_list.insert(items, reverse_dictionary[replacement])
        text_lower_list.pop(items + 1)       
    text = ''.join(text_lower_list)
    return text

#Athenian recurrent encryptiom
def Athenian_recurrent_encryptiom(text, a1_key, a2_key, b1_key, b2_key):
    dictionary = new_eng_dictionary()
    a1_key = int(a1_key)
    a2_key = int(a2_key)
    b1_key = int(b1_key)
    b2_key = int(b2_key)
    power_dictionary = len(dictionary)
    a_list = [0] * power_dictionary
    b_list = [0] * power_dictionary
    a_list[0] = a1_key
    a_list[1] = a2_key
    b_list[0] = b1_key
    b_list[1] = b2_key
    reverse_dictionary = new_eng_reverse_dictionary()
    len_text = len(text)
    text_lower = text.lower()
    text_lower_list = list(text_lower)
    for items in range(len_text):
        replacement = (a_list[items] * dictionary[text_lower_list[items]] + b_list[items]) % power_dictionary
        text_lower_list.insert(items, reverse_dictionary[replacement])
        text_lower_list.pop(items + 1)
        a_list[items+2] = (a_list[items+1] * a_list[items]) % power_dictionary
        b_list[items+2] = (b_list[items] + b_list[items + 1]) % power_dictionary
    text = ''.join(text_lower_list)
    return text

#Athenian recurrent decryptiom
def Athenian_recurrent_decryptiom(text, a1_key, a2_key, b1_key, b2_key):
    dictionary = new_eng_dictionary()
    a1_key = int(a1_key)
    a2_key = int(a2_key)
    b1_key = int(b1_key)
    b2_key = int(b2_key)
    power_dictionary = len(dictionary)
    a_list = [0] * power_dictionary
    b_list = [0] * power_dictionary
    a_list[0] = a1_key
    a_list[1] = a2_key
    b_list[0] = b1_key
    b_list[1] = b2_key
    reverse_dictionary = new_eng_reverse_dictionary()
    len_text = len(text)
    text_lower = text.lower()
    text_lower_list = list(text_lower)
    for items in range(len_text):
        gcd, x, y = extended_Euclidean_algorithm(a_list[items], power_dictionary)
        if gcd == 1:
            evv = (x % power_dictionary + power_dictionary) % power_dictionary
        else:
            evv = -1
        replacement = int(evv) * (dictionary[text_lower_list[items]] + power_dictionary - b_list[items]) % power_dictionary
        text_lower_list.insert(items, reverse_dictionary[replacement])
        text_lower_list.pop(items + 1)
        a_list[items+2] = (a_list[items+1] * a_list[items]) % power_dictionary
        b_list[items+2] = (b_list[items] + b_list[items + 1]) % power_dictionary
    text = ''.join(text_lower_list)
    return text

#Athenian encryptiom
def athenian_encryptiom(text, a_key, b_key):
    dictionary = new_eng_dictionary()
    a_key = int(a_key)
    b_key = int(b_key)
    reverse_dictionary = new_eng_reverse_dictionary()
    power_dictionary = len(dictionary)
    len_text = len(text)
    text_lower = text.lower()
    text_lower_list = list(text_lower)
    for items in range(len_text):
        replacement = (a_key * dictionary[text_lower_list[items]] + b_key) % power_dictionary
        text_lower_list.insert(items, reverse_dictionary[replacement])
        text_lower_list.pop(items + 1)
    text = ''.join(text_lower_list)
    return text

#Athenian decryptiom
def athenian_decryptiom(text, a_key, b_key):
    dictionary = new_eng_dictionary()
    a_key = int(a_key)
    b_key = int(b_key)
    reverse_dictionary = new_eng_reverse_dictionary()
    power_dictionary = len(dictionary)
    len_text = len(text)
    text_lower = text.lower()
    text_lower_list = list(text_lower)
    for items in range(len_text):
        gcd, x, y = extended_Euclidean_algorithm(a_key, power_dictionary)
        if gcd == 1:
            evv = (x % power_dictionary + power_dictionary) % power_dictionary
        else:
            evv = -1
        replacement = int(evv) * (dictionary[text_lower_list[items]] + power_dictionary - b_key) % power_dictionary
        text_lower_list.insert(items, reverse_dictionary[replacement])
        text_lower_list.pop(items + 1)
    text = ''.join(text_lower_list)
    return text

#block encryptiom
def block_encryption(text, key):
    dictionary = new_eng_dictionary()
    reverse_dictionary = new_eng_reverse_dictionary()
    power_dictionary = len(dictionary)
    counter = 0
    #len of text and key
    len_text = len(text)
    len_key = len(key)
    #lower of text and key
    text_lower = text.lower()
    key_lower = key.lower()
    #lower of text and key => lower list of text and key
    text_lower_list = list(text_lower)
    key_lower_list = list(key_lower)
    for items in range(len_text):
        if (counter >= len_key):
            counter = 0
        #setup replacement
        replacement = (dictionary[key_lower_list[counter]] + dictionary[text_lower_list[items]]) % power_dictionary
        text_lower_list.insert(items, reverse_dictionary[replacement])
        text_lower_list.pop(items + 1)       
        counter = counter + 1
    text = ''.join(text_lower_list)
    return text
#block decryption
def block_decryption(text, key):
    dictionary = new_eng_dictionary()
    reverse_dictionary = new_eng_reverse_dictionary()
    power_dictionary = len(dictionary)
    counter = 0
    #len of text and key
    len_text = len(text)
    len_key = len(key)
    #lower of text and key
    text_lower = text.lower()
    key_lower = key.lower()
    #lower of text and key => lower list of text and key
    text_lower_list = list(text_lower)
    key_lower_list = list(key_lower)
    for items in range(len_text):
        if (counter >= len_key):
            counter = 0
        #setup replacement
        replacement = (dictionary[text_lower_list[items]] - dictionary[key_lower_list[counter]]) % power_dictionary
        text_lower_list.insert(items, reverse_dictionary[replacement])
        text_lower_list.pop(items + 1)       
        counter = counter + 1
    text = ''.join(text_lower_list)
    return text

#create eng dictionary with """, " ", ".", ",", "!", "?" and numbers
def new_eng_dictionary():
    dictionary = {
        "a" : 1,
        "b" : 2,
        "c" : 3,
        "d" : 4,
        "e" : 5,
        "f" : 6,
        "g" : 7,
        "h" : 8,
        "i" : 9,
        "j" : 10,
        "k" : 11,
        "l" : 12,
        "m" : 13,
        "n" : 14,
        "o" : 15,
        "p" : 16,
        "q" : 17,
        "r" : 18,
        "s" : 19,
        "t" : 20,
        "u" : 21,
        "v" : 22,
        "w" : 23,
        "x" : 24,
        "y" : 25,
        "z" : 26,
        " " : 27,
        "," : 28,
        "." : 29,
        "!" : 30,
        "?" : 31,
        "\"" : 32,
        ":" : 33,
        "1" : 34,
        "2" : 35,
        "3" : 36,
        "4" : 37,
        "5" : 38,
        "6" : 39,
        "7" : 40,
        "8" : 41,
        "9" : 42,
        "0" : 43
    } 
    return dictionary

#create reverse eng dictionary with """, " ", ".", ",", "!", "?" and numbers
def new_eng_reverse_dictionary():
    dictionary = {
        1 : "a",
        2 : "b",
        3 : "c",
        4 : "d",
        5 : "e",
        6 : "f",
        7 : "g",
        8 : "h",
        9 : "i",
        10 : "j",
        11 : "k",
        12 : "l",
        13 : "m",
        14 : "n",
        15 : "o",
        16 : "p",
        17 : "q",
        18 : "r",
        19 : "s",
        20 : "t",
        21 : "u",
        22 : "v",
        23 : "w",
        24 : "x",
        25 : "y",
        26 : "z",
        27 : " ",
        28 : ",",
        29 : ".",
        30 : "!",
        31 : "?",
        32 : "\"",
        33 : ":",
        34 : "1",
        35 : "2",
        36 : "3",
        37 : "4",
        38 : "5",
        39 : "6",
        40 : "7",
        41 : "8",
        42 : "9",
        43 : "0",
    } 
    return dictionary

text = ""
key = ""
a_key = 0
b_key = 0
print("If you want simple de/encrypting 1, 2 if Athenian cipherasd, 3 if Affine recurrent cipher, 4 if block cipher")
a1 = int(input())
if(a1 == 4):
    print('If you want to encrypt the text, enter 1, if you want to decrypt, enter 2')
    a2 = int(input())
    if(a2 == 1):
        print('Enter the text')
        text = input()
        print('Enter the key')
        key = input()
        print(block_encryption(text, key))
    if(a2 == 2):
        print('Enter the text')
        text = input()
        print('Enter the key')
        key = input()
        print(block_decryption(text, key))
if(a1 == 2):
    print('If you want to encrypt the text, enter 1, if you want to decrypt, enter 2')
    a2 = int(input())
    if(a2 == 1):    
        print('Enter the first numeric key that is greater than 1')
        a_key = input()
        print('Enter a second numeric key that is greater than 1')
        b_key = input()
        print('Enter a text')
        text = input()
        if(int(a_key) < 2 or int(b_key) < 2):
            print("ERROR")
            exit(0)
        print(athenian_encryptiom(text, a_key, b_key))
    if(a2 == 2):
        print('Enter the first numeric key that is greater than 1')
        a_key = input()
        print('Enter a second numeric key that is greater than 1')
        b_key = input()
        print('Enter a text')
        text = input()
        if(int(a_key) < 2 or int(b_key) < 2):
            print("ERROR")
            exit(0)
        print(athenian_decryptiom(text, a_key, b_key))
if(a1 == 3):
    print('If you want to encrypt the text, enter 1, if you want to decrypt, enter 2')
    a2 = int(input())
    if(a2 == 1):    
        print('Enter the first numeric a key that is greater than 1')
        a1_key = input()
        print('Enter the second numeric a key that is greater than 1')
        a2_key = input()
        print('Enter a first numeric b key that is greater than 1')
        b1_key = input()
        print('Enter a second numeric b key that is greater than 1')
        b2_key = input()
        print('Enter a text')
        text = input()
        if(int(a1_key) < 2 or int(b1_key) < 2 or int(b2_key) < 0 or int(a2_key) < 0):
            print("ERROR")
            exit(0)
        print(Athenian_recurrent_encryptiom(text, a1_key, a2_key, b1_key, b2_key))
    if(a2 == 2):
        print('Enter the first numeric a key that is greater than 1')
        a1_key = input()
        print('Enter the second numeric a key that is greater than 1')
        a2_key = input()
        print('Enter a first numeric b key that is greater than 1')
        b1_key = input()
        print('Enter a second numeric b key that is greater than 1')
        b2_key = input()
        print('Enter a text')
        text = input()
        if(int(a1_key) < 2 or int(b1_key) < 2 or int(b2_key) < 0 or int(a2_key) < 0):
            print("ERROR")
            exit(0)
        print(Athenian_recurrent_decryptiom(text, a1_key, a2_key, b1_key, b2_key))
if(a1 == 1):
    print('If you want to encrypt the text, enter 1, if you want to decrypt, enter 2')
    a2 = int(input())
    if(a2 == 1):
        print('Enter the text')
        text = input()
        print('Enter the key')
        key = input()
        print(simple_substitution_encryptiom(text, key))
    if(a2 == 2):
        print('Enter the text')
        text = input()
        print('Enter the key')
        key = input()
        print(simple_substitution_decryptiom(text, key))