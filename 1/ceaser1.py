ofile = input("enter the file name: ")
file = open(ofile, "r")

text = file.read()

print(text)

key = int(9)

def encrypt(text, key):
	result = ""
	
	for i in range(len(text)):
		char = text[i]
		
		if(char == ' '):
			result = result + ' '
		elif(char.isupper()):
			result = result + chr((ord(char) + key - 65) % 26 + 65)
		elif(char.islower()):
			result = result + chr((ord(char) + key - 97) % 26 + 97)
		else:
			result = result + char;
		
	return result


wfile = input("enter write file name: ")
file2 = open(wfile, "w")

file2.write(encrypt(text,key))
file2.close()

print(encrypt(text, key))
