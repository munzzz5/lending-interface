import random
import math
import numpy as np
import time
def colChange(matrix,c1,c2,kr3):
    for i in range(0,kr3):
        temp=matrix[c1][i]
        matrix[c1][i]=matrix[c2][i]
        matrix[c2][i]=temp
    return matrix
def fibon(m,n):
    a=[0]
    if n==1:
        if n==2:
            a.insert(1,1)
            a.insert(2,1)
        else:
            print("Enter a higher value than One for Shuffling")
    else:
        a.insert(1,1)
        a.insert(2,1)
        x=1
        y=1
        for i in range(3,m+n-1):
            
            z=x+y
            a.insert(i,z)
            x=y
            y=z
    return a[m-1:m+n]
def keyGen(pltext):
    k1=random.randrange(2,30)
    l1=len(str(k1))
    k2=random.randrange(2,30)
    l2=len(str(k2))
    k3=math.ceil(math.sqrt(len(pltext)))
    l3=len(str(k3))

    kf=str(k1)+str(k2)+str(k3)
    lf=str(l1)+str(l2)+str(l3)
    return kf,lf
def keySplit(k,l):
    lr1=int(l[0])
    lr2=int(l[1])
    print(lr1,lr2)
    ss=""
    for i in range(2,len(l)):
        ss=ss+l[i]

    lr3=int(ss)
    
    ss1=""
    for i in range(0,lr1):
        ss1=ss1+k[i]
    kr1=int(ss1)
    ss2=""
    for i in range(lr1,(lr1+lr2)):
        ss2=ss2+k[i]
    kr2=int(ss2)
    ss3=""
    for i in range((lr1+lr2),(lr1+lr2+lr3)):
        ss3=ss3+k[i]
    kr3=int(ss3)
    return [kr1,kr2,kr3]
def encrypt(pltext,k,l):
    count=0
    list1=list(pltext)
    list2=[]
    kr=keySplit(k,l)
    kr1=kr[0]
    kr2=kr[1]
    kr3=kr[2]
    print("Key parts:",kr1,kr2,kr3,sep='*')
    for i in range(0,kr3):
        list2.append([])
    for i in range(0,kr3):
        for j in range(0,kr3):
            if(count<len(pltext)):
                list2[j].append(list1[count])
                count=count+1
            else:
                list2[j].append("X")
    if(kr1%2==0):
        fib=fibon(kr2,kr1)
        fib=[x%kr3 for x in fib]
        print(fib)
    else:
        kr1=kr1+1
        fib=fibon(kr2,kr1)
        print("Original fibonacci series:",fib)
        fib=[x%kr3 for x in fib]
        print("fibonacci series modulus by dimension of matrix:",fib)
    c1=fib[0::2]
    c2=fib[1::2]
    print("col1 to change:",c1)
    print("col2 to change:",c2)
    for i in range(len(c1)):
        finalMatrix=colChange(list2,c1[i],c2[i],kr3)
        print(finalMatrix)
    encryptList=[]
    for i in range(0,kr3):
        for j in range(0,kr3):
            encryptList.append(finalMatrix[i][j])
    print(pltext,end='\n')
    encryptText=''.join(encryptList)
    print(encryptText)
    return encryptText

def decrypt(cipher,k,l):
    kr=keySplit(k,l)
    list1=list(cipher)

    kr1=kr[0]
    kr2=kr[1]
    kr3=kr[2]
    list2=np.full((kr3,kr3),'k')

    

    count=0
    for i in range(0,kr3):
        for j in range(0,kr3):
            list2[i][j]=list1[count]
            count=count+1
    if(kr1%2==0):
        fib=fibon(kr2,kr1)
        fib=[x%kr3 for x in fib]
        print(fib)
    else:
        kr1=kr1+1
        fib=fibon(kr2,kr1)
        print("Original fibonacci series:",fib)
        fib=[x%kr3 for x in fib]
        print("fibonacci series modulus by dimension of matrix:",fib)
    c1=fib[0::2]
    c2=fib[1::2]
    c1.reverse()
    c2.reverse()

    print("col1 decry to change:",c1)
    print("col2 decry to change:",c2)
    for i in range(len(c1)):
        finalMatrix=colChange(list2,c1[i],c2[i],kr3)
        print("decrypted matrix",finalMatrix)
    decryptList=[]
    for i in range(0,kr3):
        for j in range(0,kr3):
            decryptList.append(finalMatrix[j][i])
    print(cipher,end='\n')
    decryptText=''.join(decryptList)
    print(decryptText)
for i in range(10):
    start=time.time()
    plain_text=input("Enter a String")
    o1,o2=keyGen(plain_text)
    print(o1,o2,sep=';')
    cipher=encrypt(plain_text,o1,o2)
    decrypt(cipher,o1,o2)
    print(time.time()-start)
