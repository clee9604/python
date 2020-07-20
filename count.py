fname = input("Enter the name of the file: ")
file = open(fname, "r")

data = file.read()

fkey = data.count("e")
skey = data.count("t")



numChar = len(data)

print(fkey)
print(skey)
print(numChar)
