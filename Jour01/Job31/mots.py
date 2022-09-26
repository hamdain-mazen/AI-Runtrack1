my_word = input("write a single word with only letters: ")

for c in my_word:
    if ord(c) >= 97 and ord(c) <= 122 :
            print('ok')
    else :
             print("pas bon")
