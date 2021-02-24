astr = "---i love zfdulardz strings---"
str1 = "zfd"
str2 = "reg"

"""
lstrip, rstrip, strip function
"""
print(astr.lstrip("-"))
print(astr.rstrip("-"))
print(astr.strip("-"))

"""
min and max
"""

print(f"min is {min(astr)}")
print(max(astr))

"""
maketrans is used to map contents of str1 to str2 for str: i.e. python remembers the mapping to be used later by translate function
translate replaces the mapped str in the new string (here str)
"""

mapped = astr.maketrans(str1,str2)
print(f"after translate is {astr.translate(mapped)}")

"""
replace function: replaces a complete string
difference between replace and translate: replaces entire string, translate replaces char by char
"""
print("replaced ",astr.replace(str1, str2))
"""
A Caesar cipher is a simple substitution cipher in which each letter of the plain text is substituted with a letter found by moving n places down the alphabet
write a function that accepts two arguments, a plain-text message and a number of letters to shift in the cipher. 
The function will return an encrypted string with all letters transformed and all punctuation and whitespace remaining unchanged.
"""
import string

def caesarCipher(plain_text, shift_letters):
    x = string.ascii_lowercase # x has all the lowercase letters of the alphabet
    mask = x[shift_letters:]+x[:shift_letters] # now mask has the letters shifted by the shift_letters number
    transtab = str.maketrans(x,mask) # str is a builtin function, now mapping is done between before and after letters are shifted
    return plain_text.translate(transtab) # now the replacement happens in the original string

shiftedceasar = caesarCipher("sdjnsa kndnr", 4)
print("shifted ceasar is", shiftedceasar)

