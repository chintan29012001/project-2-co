from math import *

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

def diff_bin(a,b):
    x=len(a)
    y=len(b)
    z=max(a,b)
    a=a[::-1]
    b=b[::-1]
    i=0
    j=0
    d=""
    bitbin=0
    while(i<x or j<y):
        if(i<x):
            ai=int(a[i])
        else:
            ai=0
        if(j<y):
            bj=int(b[j])
        else:
            bj=0
        
        bitd=ai^bj^bitbin
        bitout=bitbin&int(not(ai^bj))|(int(not(ai))&bj)        
        bitbin=bitout
        d+=str(bitd)
        i+=1
        j+=1
        
    return d[::-1]

def right_shift(A,q,qn):
    qn=q[-1]
    q=A[-1]+q[:-1]
    A=A[0]+A[:-1]
    return A,q,qn

def bin_to_int(x):
    a=x
    flg=0
    if(x[0]=="1"):
        flg=1
        a=""
        i=0
        while(i<len(x)):
            a+=str(int(not(int((x[i])))))
            i+=1
    i=0
    x=0
    a=a[::-1]
    while(i<len(a)):
        x+=2**(i)*int(a[i])
        i+=1
    if(flg==0):
        return x
    elif(flg==1):
        return -x-1



def booth(m,q):
    qn="0"
    n=max(len(m),len(q))
    A="0"*(n)
    i=1
    while(n>0):
        print(str(i)+"th step")        
        print('A '+A)
        print('q '+q)
        print('q-1 '+qn)
        if((q[-1]=="1")&(qn=="0")):
            print('diff')
            A=diff_bin(A,m)
        elif((qn=="1")&(q[-1]=="0")):
            print('add')
            A=add_bin(A,m)
        A,q,qn=right_shift(A,q,qn)
        n-=1
        i+=1
    print('Ans '+q)
    ans=bin_to_int(A+q)
    print("integer of ans "+str(ans))
    return str(ans)

a=float(input())
x=a
ad=a-floor(a)
if(ad>0):
    ae=len(str(ad))-3
else:
    ae=len(str(ad))-4

b=float(input())
y=b
bd=b-floor(b)
if(bd>0):
    be=len(str(ad))-3
else:
    be=len(str(ad))-4


a=int_to_bin(int(a*10**(ae)))
b=int_to_bin(int(b*10**(be)))

while(len(a)>len(b)):
    b=b[0]+b
while(len(a)<len(b)):
    a=a[0]+a

print(float(booth(a,b))/10**(ae+be))
print(x*y)



