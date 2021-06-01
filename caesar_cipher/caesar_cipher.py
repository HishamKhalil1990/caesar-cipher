import nltk
nltk.download('words',quiet=True)
nltk.download('names',quiet=True)
from nltk.corpus import words,names
import re
words_list = words.words()
name_list = names.words()

def encrypt(plain_text,key):
    new_string = ""
    for char in plain_text:
        if re.match("[A-Z]",char):
            new_char = 65 + ((ord(char) - 65) + key) % 26
            new_string += chr(new_char)
        elif re.match("[a-z]",char):
            new_char = 97 + ((ord(char) - 97) + key) % 26
            new_string += chr(new_char)
        else:
            new_string += char
    return new_string

def decrypt(plain_text,key):
    return encrypt(plain_text,-key)

def crack(plain_text):
    string_list1 = []
    percentages_list = []
    for num in range(27):
        string_list1.append(decrypt(plain_text,-num))
    string_list = [string.split(" ") for string in string_list1]
    for str_list in string_list:
        percentage = count(str_list) / len(str_list) * 100
        percentages_list.append(percentage)
    maximum_value = max(percentages_list)
    index = percentages_list.index(maximum_value)
    return string_list1[index]

def count(str_list):
    counter = 0
    for word in str_list:
        if word.lower() in words_list or word in name_list:
            counter += 1
    return counter

if __name__ == "__main__":
    encrepted = encrypt('A dead duck doesn\'t fly backward',13)
    encrepted2 = encrypt('Cats are good pets, for they are clean and are not noisy',37)
    encrepted3 = encrypt('Writing a list of random sentences is harder than I initially thought it would be',22)
    encrepted4 = encrypt('He quietly entered the museum as the super bowl started',116)
    print(encrepted)
    print(encrepted2)
    print(encrepted3)
    print(encrepted4)
    print(decrypt(encrepted,13))
    print(decrypt(encrepted2,37))
    print(crack(encrepted))
    print(crack(encrepted2))
