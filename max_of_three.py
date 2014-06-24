#exe 2
#function to return the largest 
#among three numbers

def max_three(a, b, c):
    if a>=b>=c:
        return a
    elif b>= a>=c:
        return b
    else:
        return c
        
print max_three(4,5,6)
print max_three(9,8,5)
print max_three(3,8,5)

#tests passed
