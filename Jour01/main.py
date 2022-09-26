10 + 3
13 * 3
print(10+3)





def Add(x,y):
    r = x+y
    return r
print(Add(2,2))




name = input("Enter your name: ")
print("Hello", name + "!!")



for number in range(5):
    listnum = []
    number =int(input("Entrez un nombre : "))
    listnum.append(number)
    #sort the number
    listnum.sort()
    # show the sorted numbers
    print (listnum)



for fizzbuzz in range(101):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
    elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
    elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
    print(fizzbuzz)
