#exe5.py
#a function that... double every consonant and place an occurrence of
#"o" in between. For example, translate("this is fun") should return 
#the string"tothohisos isos fofunon".

def translate_(string):
    real_sent = []
    for s in string:
        if s in 'qwrtypsdfghjklzxcvbnm':
            g = s+"o"+s
            real_sent.append(g)
        else:
            real_sent.append(s)
    final_string = ''.join(real_sent)
    return final_string
    
    
print translate_("this is for fun")


#test passed
