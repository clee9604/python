fname = input("Enter the name of file:")
file = open(fname, "r")

data = file.read()

test = "abcdefg"

all_freq = {}

for i in data:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

print(str(all_freq))
