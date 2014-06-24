#exe4.py
#a function which returns True for a character being a vowel

def vowel(char_):
    if char_=="":
        return False   #exception created
    elif char_ in 'aeiou':
        return True
    else:
        return False
        
print vowel("") #this returned True for the first run...creating exception
print vowel("a")
print vowel("n")
print vowel("v")

#test passed
