file = open("data.txt", "r")
data = file.read()
file.close()
data = data.lower()

for x in list(data):
    data.count(x)
    print(x,'= is', data.count(x))

