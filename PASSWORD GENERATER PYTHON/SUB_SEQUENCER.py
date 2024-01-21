
def Subsequence_checker(s):
    l=[]
    for i in range(len(s)):
        for j in range(i, len(s)):
            global sub
            sub=""
            for k in range(i, (j + 1)):
                sub+=s[k]
            l.append(sub)
            
    
    for i in l:
        if len(i)==1 or len(i)==2:
            l.remove(i)


    s=['asdf','qwerty','123','QWERTY','ASDF','1234','12345','123456','1234567','12345678','123456789']
    t_val=None
    substring2suggest=""
   
    for i in l:
        if i in s:
            t_val=True
            substring2suggest=i
    return t_val,substring2suggest
