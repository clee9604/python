ofile = input("enter the file name: ")
file = open(ofile, "r")

text = file.read()

print(text)

fkey = text.count("e")
skey = text.count("t")

Ekey = int(fkey) / 5
Tkey = int(skey) / 20

key = int(Ekey) + int(Tkey)

print("total key is:")
print(key)

def encrypt(text, key):
	result = ""
	
	for i in range(len(text)):
		char = text[i]
		
		if(char == ' '):
			result = result + ' '
		elif(char.isupper()):
			if(ord(char)-key<65):
				result = result + chr(ord(char) + (26 -key))
			else:
				result = result + chr(ord(char) - key)
		elif(char.islower()):
			if(ord(char)-key<97):
				result = result + chr(ord(char) + (26-key))
			else:
				result = result + chr(ord(char) - key)
		else:
			result = result + char;
		
	return result


wfile = input("enter write file name: ")
file2 = open(wfile, "w")

file2.write(encrypt(text,key))
file2.close()

print(encrypt(text, key))
