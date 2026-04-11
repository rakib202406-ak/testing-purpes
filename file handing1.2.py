f = open("s.txt","a")
f.write(" now he is fine")
f.close()

#open and read the file after the overwriting:
f = open("s.txt","r")
print(f.read())