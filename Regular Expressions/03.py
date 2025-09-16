# search - (pattern,string,flags)
import re
pattern = "apple"
if re.search(pattern,"ballapple"):
    print(True)
else:
    print(False)
# search() function can search for the string found in the pattern or not
# match() function can match the first 5 characters of the string.


