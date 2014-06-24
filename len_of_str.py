#exe3.py
#function to return length of a string
#dont consider len() function

def len_(string):
    length=0
    for i in string:
        length += 1
    return length
    
print len_("")
print len_("people")
print len_("\n")

#tests passed
