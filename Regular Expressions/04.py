# sub(pattern,repl,string,count,flags) - replace an word from the string
import re
string = "It is a dog"
pattern = "dog"
print(re.sub(pattern,"cat",string,count=0))