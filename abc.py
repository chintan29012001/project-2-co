def add_bin(a,b):
    x=len(a)
    y=len(b)
    z=max(a,b)
    a=a[::-1]
    b=b[::-1]
    i=0
    j=0
    s=""
    bitc=0
    while(i<x or j<y):
        if(i<x):
            ai=int(a[i])
        else:
            ai=0
        if(j<y):
            bj=int(b[j])
        else:
            bj=0
        bits=ai^bj^bitc
        bitc=ai&bj | bitc&(ai^bj)
        s+=str(bits)
        i+=1
        j+=1
    return s[::-1]

def int_to_bin(x):
    a=""
    flg=0
    if(x<0):
        flg=1
        x=-x
    
    while(x>0):
        a+=str(x%2)
        x//=2
    
    if(flg==1):
        i=0
        b=""
        while(i<len(a)):
            b+=str(int(not(int((a[i])))))
            i+=1
        b=b[::-1]
        a=add_bin(b,"1")
    if(flg==1):
        return "1"+a
    else:
        return "0"+a[::-1]

print(int_to_bin(-1024))