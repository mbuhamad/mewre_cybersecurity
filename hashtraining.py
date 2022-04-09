# Mashal Buhamad 2022 #
# Hash function taking input from argv
from sys import argv as inp
inp.pop(0)
inp=(' '.join(inp))
print (inp)
import hashlib
m=hashlib.sha256()
text=inp.encode ()
m.update(text)
dig=m.hexdigest()
print(dig)
n=hashlib.md5()
n.update(text)
dig2=n.hexdigest()
print(dig2)