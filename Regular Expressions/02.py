# match()- (pattern,string,flags)
import re
pattern = "apples"
if re.match(pattern,'apple'):
    print(True)
else:
    print(False)

# findall(pattern,strings,flags)
import re
pattern = "Mango"
string = re.findall('Mango',pattern)
print(string)
