import re
f = open("Indonesia.txt","r",encoding="latin1")
teks = f.read()
f.close()
cocok = r'me\w+'
output = re.findall(cocok,teks)
print(output)
