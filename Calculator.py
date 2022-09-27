a=input("Enter the values:\n")
b=[*a]
for values in b:
    if values.isdigit()==True:
        ind=b.index(values)
        val=float(values)
        b.remove(values)  
        b.insert(ind,val)
        
    #else:
     #   b.remove(values)
print(b)

if '/' in b:
    op=b.index('/')
    total=b[op-1] / b[op+1]
    if len(b)>=3:
        b.pop(op+1)    
        b.pop(op)
        b.pop(op-1)
        
    b.insert(op-1,total)

if '*' in b:
    op=b.index('*')
    total=b[op-1] * b[op+1]
    if len(b)>=3:
        b.pop(op+1)    
        b.pop(op)
        b.pop(op-1)
        
    b.insert(op-1,total)

if '+' in b:
    op=b.index('+')
    total=b[op-1] + b[op+1]
    if len(b)>=3:
        b.pop(op+1)    
        b.pop(op)
        b.pop(op-1)
        
    b.insert(op-1,total)

if '-' in b:
    op=b.index('-')
    total=b[op-1] - b[op+1]
    if len(b)>=3:
        b.pop(op+1)    
        b.pop(op)
        b.pop(op-1)
        
    b.insert(op-1,total)

 
#if '%' in list:
#    op=b.index('%')
#    total=b[op-1] % b[op+1]
#    b.pop(op-1)
#    b.pop(op+1)
#    b.insert(0,total)
    
print(total)
