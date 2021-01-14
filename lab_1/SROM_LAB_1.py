def line_prt():
    print("=================================================================")
def plus(A = [], B=[]):
    C = []
    cel = 0
    if len(A)>=len(B):
        min_len = len(B)
    else:
        min_len = len(A)
    for i in range(0,2048):
        value = A[i]+ B[i]+cel
        ost = value%16
        cel = value//16
        C.append(ost)
    return C
def minus(A = [], B = []):
    C = []
    for i in range(0,2048):
        value = A[i] - B[i]
        if value < 0:
            if i!=2047:
                value += 16
                A[i+1]-=1
        C.append(value)
    if C[2047] < 0:
        print("Error")
        return [-1]
    return C


def multy(A = [], B = []):
    count = 0
    count_2 = 0
    C = [0]*max([len(A),len(B)])*2
    for i in range(0,len(B)):
        count = 0
        for j in A:
            value = B[i]*j
            ost = value%16
            cel = value//16
            C[i+count] +=ost
            if i !=(len(C)-1):
                C[i+count+1]+=cel   
            count+=1
    for i in range(0,len(C)):
        value = C[i]
        ost = value%16
        cel = value//16
        C[i] = ost
        if i !=(len(C)-1):
            C[i+1] += cel
    if C[len(C)-1]!=0:
        print("Er")
    return C


def multy_pow(A = [], B = []):
    count = 0
    count_2 = 0
    C = [0]*max([len(A),len(B)])*2
    for i in range(0,len(B)):
        count = 0
        for j in A:
            value = B[i]*j
            ost = value%16
            cel = value//16
            C[i+count] +=ost
            if i !=(len(C)-1):
                C[i+count+1]+=cel   
            count+=1
    for i in range(0,len(C)):
        value = C[i]
        ost = value%16
        cel = value//16
        C[i] = ost
        if i !=(len(C)-1):
            C[i+1] += cel
    if len(C)> len(turn(C)):
        num_min = len(turn(C))
        for i in range(num_min,len(C)):
            C.pop(num_min)
    return C


def sr(A = [], B = []):
    if len(A) > len(B):
        return sr(B,A)
    for i in range(len(A)-1,-1,-1):
        if A[i]>B[i]:
            return True
        elif A[i] == B[i]:
            continue
        elif B[i]>A[i]:
            return False
        else:
            return True

        
def equal(A = [], B = []):
    count = 0
    for i in range(len(A)-1,-1,-1):
        if A[i]==B[i]:
            count+=1
    if count == len(A):
        return True
    else:
        return False

    
def convert(num = 0):
    A = []
    while num >=15:
        ost = num%16
        num//=16
        A.append(ost)
    A.append(num)
    if A[len(A)-1] == 0:
        A.pop(len(A)-1)
    A = A+[0]*(2048-len(A))
    return A


def convert_rev(A = []):
    stek = 0
    count = 0
    for i in range(len(A)-1,-1,-1):
        if A[i] !=0:
            break
        else:
            count+=1
    for i in range(len(A)-count-1,-1,-1):
        stek+= A[i]*(16**i)
    return stek


def DivMod(A = [], B=[]):
    R = A.copy()
    Q = []
    count = 0
    count_1 = 0
    log = False
    for i in range(len(A)-1,-1,-1):
        if A[i] != 0 and not(log):
            log = True
        elif A[i] == 0 and not(log):
            count+=1
    for i in range(len(A)-count-1,-1,-1):
        count_1 = 0
        if sr(B,convert(A[i])):
            if i!=0:
                #print(A)
                A[i-1]+=A[i]*16
            else:
            	break     	
        while(sr(convert(A[i]),B) or equal(convert(A[i]),B)):
            A[i] = convert_rev(minus(convert(A[i]),B))
            count_1+=1
        Q.append(count_1)
        if i !=0 and i !=len(A)-count-1 and count_1!=0:
       	    A[i-1] += A[i]*16
    #print(convert(A[0])) # остаток не забудь!!!
    
    count_2 = 0
    for i in range(len(Q)):
        if Q[i] == 0:
            count_2+=1
        else:
            break
    for i in range(count_2):
        Q.remove(0)
    Q.reverse()
    if len(Q) == 0:
        Q.append(0)
    return Q
    
    
    
def Mod(A = [], B=[]):
    R = []
    Q = []
    count = 0
    count_1 = 0
    log = False
    for i in range(len(A)-1,-1,-1):
        if A[i] != 0 and not(log):
            log = True
        elif A[i] == 0 and not(log):
            count+=1
    for i in range(len(A)-count-1,-1,-1):
        count_1 = 0
        if sr(B,convert(A[i])):
            if i!=0:
                #print(A)
                A[i-1]+=A[i]*16
            else:
            	break
            	
        while(sr(convert(A[i]),B) or equal(convert(A[i]),B)):
            A[i] = convert_rev(minus(convert(A[i]),B))
            count_1+=1
        Q.append(count_1)
        if i !=0 and i !=len(A)-count-1 and count_1!=0:
       	    A[i-1] += A[i]*16
    R = convert(A[0])
    
    return R
    
def turn(A = []):
    log = False
    count = 0
    C = []
    string = ""
    #print(len(A))
    for i in range(len(A)-1,-1,-1):
        if A[i] != 0 and not(log):
            log = True
        elif A[i] == 0 and not(log):
            count+=1
    #print(count)
    for i in range(0,len(A)-count):
        C.append(A[i])
    for i in reversed(C):
        if i == 10:
            string+="a"
        elif i == 11:
            string+="b"
        elif i == 12:
            string+="c"
        elif i == 13:
            string+="d"
        elif i == 14:
            string+="e"
        elif i == 15:
            string+="f"
        else:
            string+=str(i)
    if len(string) == 0:
        string+="0"
    if string == "-1":
        string = ""
    return string 
def power(A = [], B = []):
    C = [1]+[0]*2047
    R = []
    D = turn(B)
    string = ""
    for i in D:
        if i == "0":
            string+="0000"
        if i == "1":
            string+="0001"
        if i == "2":
            string+="0010"
        if i == "3":
            string+="0011"
        if i == "4":
            string+="0100"
        if i == "5":
            string+="0101"
        if i == "6":
            string+="0110"
        if i == "7":
            string+="0111"
        if i == "8":
            string+="1000"
        if i == "9":
            string+="1001"
        if i == "a":
            string+="1010"
        if i == "b":
            string+="1011"
        if i == "c":
            string+="1100"
        if i == "d":
            string+="1101"
        if i == "e":
            string+="1110"
        if i == "f":
            string+="1111"
    for i in string:
        R.append(int(i))
    for i in range(len(R)-1,-1,-1):
        if R[i] == 1:
            C = multy_pow(C,A)
        A = multy_pow(A,A)
    return C
def squer(A = []):
    C = multy(A,A)
    return C
def HEX(a = ""):
    A = []
    for i in reversed(a):
        if i == "a":
            A.append(10)
        elif i == "b":
            A.append(11)
        elif i == "c":
            A.append(12)
        elif i == "d":
            A.append(13)
        elif i == "e":
            A.append(14)
        elif i == "f":
            A.append(15)
        else:
            A.append(int(i))
    A = A + [0]*(2048 - len(A))
    #print(A)
    return A
def evklid(A = [], B = []):
    while B!=[0]*2048:
        T = B.copy()
        B = Mod(A,B)
        A = T.copy()
    return A
def ICM(A = [], B = []):
    C = DivMod(multy(A,B),evklid(A,B))
    return C

def baret(C = [], M = []):
    k = len(turn(M))
    st = len(turn(C)) - (k - 1)
    q2 = turn(C)[:st]
    u = (16**(2*len(M)))
    q2 = HEX(q2)
    k2 = HEX("2")
    K = HEX(str(k))
    a = multy(k2,K)
    B = HEX("10")
    B = power(B,a)
    u = DivMod(B,M)
    q = DivMod(C,M)
    print(turn(q))
    q2 = multy(q2,u)
    st = len(turn(q2))-(k+1)
    q1 = turn(q2)[:st]
    q1 = HEX(q1)
    print(q)
    r1 = multy(q,M)
    r = minus(C,r1)
    while sr(r,M):
        r = minus(r,M)
    return r

def plus_mod(A = [], B = [], C = []):
    D = plus(A,B)
    print(turn(D))
    Q = Mod(D,C)
    return Q

def minus_mod(A = [], B = [], C = []):
    D = minus(A,B)
    print(turn(D))
    Q = Mod(D,C)
    return Q

def multy_mod(A = [], B = [], C = []):
    return Mod(multy(A,B),C)

def sqr_mod(A = [], B = [], C = []):
    D = squer(A)
    print(turn(D))
    Q = Mod(D,C)
    return Q
def power_mod(A = [], B = [], FTP= []):
    C = [1]+[0]*2047
    R = []
    D = turn(B)
    string = ""
    for i in D:
        if i == "0":
            string+="0000"
        if i == "1":
            string+="0001"
        if i == "2":
            string+="0010"
        if i == "3":
            string+="0011"
        if i == "4":
            string+="0100"
        if i == "5":
            string+="0101"
        if i == "6":
            string+="0110"
        if i == "7":
            string+="0111"
        if i == "8":
            string+="1000"
        if i == "9":
            string+="1001"
        if i == "a":
            string+="1010"
        if i == "b":
            string+="1011"
        if i == "c":
            string+="1100"
        if i == "d":
            string+="1101"
        if i == "e":
            string+="1110"
        if i == "f":
            string+="1111"
    for i in string:
        R.append(int(i))
    for i in range(len(R)-1,-1,-1):
        if R[i] == 1:
            C = Mod(multy_pow(C,A),FTP)
        A = Mod(multy_pow(A,A),FTP)
    return C
