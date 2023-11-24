
# Tamrin Jalase dovom 



a = int(input("Enter a :"))
b = int(input("Enter b :"))
Sum = a + b
print(Sum)


# 2


a = int(input("Enter a : "))
b = int(input("Enter b : "))

if a > b:
    print("First Num is bigger :%s ! " %(a))
elif b > a : 
    print("Second Num is bigger : %s! "%(b))
else: 
    print("two numbers are equal")
    


# 3


a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a>b and a>c:
    print("First Num is bigger :%s ! " %(a))
elif b>a and b>c :
    print("Second Num is bigger : %s! "%(b))
elif c>a and c>b :
    print("3th Num is bigger : %s! "%(c))
else :
    print("3 Nums are equal")


# 5


Max = int(input("Enter First Num : "))
counter = 1

while counter <100 :
    Num1 = int(input("Enter Num :"))
    counter += 1 
    if Num1 >Max :
        Max = Num1
print(Max)


# 6


Num1 = int(input("Enter First Num :"))
Max = Num1 
Min = Num1 
count = 1 

while count<100:
    Num2 = int(input("Enter Num2 : "))
    if Num2 > Max :
        Max = Num2
    elif Num2<Min :
        Min = Num2 
    count +=1 
print("Max is %s"%(Max))
print("Min is %s"%(Min))
    

# d


L1 = []

for x in range(0,10):
    L1.append(int(input("Enter Num :")))

print(L1)
def sort(get_list):
    for i in range(1, len(get_list)):
        if(get_list[i]<get_list[i-1]):
            j = i 
            while L1[j] < get_list[j-1] and j>0:
                get_list[j],get_list[j-1] = get_list[j-1], get_list[j]
                j = j-1
    return get_list

print(sort(L1))


# Jalase sevom 

# 8



L1 = []

for x in range(0,10):
    L1.append(int(input("Enter Num :")))

print(L1)
def sort(get_list):
    for i in range(1, len(get_list)):
        if(get_list[i]>get_list[i-1]):
            j = i 
            while L1[j] >get_list[j-1] and j>0:
                get_list[j],get_list[j-1] = get_list[j-1], get_list[j]
                j = j-1
    return get_list

print(sort(L1))
        


# 9


a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
else:
    Print("3 Nums are equal ")



 # Jalase 4

# 10


Max = int(input("Enter Num :"))

for i in range (1,10):
    Num = int(input("Enter Num :"))
    if Num >Max :
        Max = Num 
print(Max)


# In[11]:


Num = int(input("Enter Num :"))

if (Num%2== 0):
    print("Even")
else :
    print("Add")


# 12


Num1 = int(input("Enter First Num :"))
Num2 = int(input("Enter Second Num :"))
L1 = []
for i in range(Num1+1,Num2):
    if (i%2 ==0):
        L1.append(i)
print(L1)


# 14


Num = int(input("Enter Num :"))
count = 0 

for i in range(2,Num):
    if (Num%i==0):
        count += 1 

if count > 0 :
    print("H")
else:
    print("F")
    


# 15


a = int(input("Enter a :"))
b = int(input("Enter b :"))
L1 = []
count = 0

if a > b :
    a = a+b
    b = a-b
    a = a-b

for numb in range(a+1, b):
    for j in range(2,numb):
        if (numb%j==0):
            count += 1 
            break
        if count != 0 :
            L1.append(numb)
            break
print(L1)
                
        


# Jalase 5 

# 15


Num1 = int(input("Enter First Num :"))
L1 = []
count = 0

if Num1 > Num2 :
    Num1 = Num1+Num2
    Num2 = Num1-Num2
    Num1 = Num1-Num2

    
b = 0
for i in range(1, Num1+1):
    if (Num1 % i == 0):
        b += i 

if (b ==Num1*2) :
    print("Yes")
else:
    print("No")


# 27


Num1 = int(input("Enter First Num :"))
Num2 = int(input("Enter Second Num :"))
L1 = []


if Num1 > Num2 :
    Num1 = Num1+Num2
    Num2 = Num1-Num2
    Num1 = Num1-Num2

for i in range (Num1, Num2+1):
    count = 0
    for j in range(1,i+1):
        if (i%j ==0):
            count += j  
    if (count== 2*i):
        print("True")
        
    else:
        print("False")
        
print(L1)


# 11




Num1 = int(input("Enter Num1 :"))
Num2 = int(input("Enter Num2 :"))
L1 = []

if Num1 > Num2 :
    Num1 = Num1+Num2
    Num2 = Num1-Num2
    Num1 = Num1-Num2

if (Num1%2 == 0):
    for i in range(Num1+2, Num2,2):
        L1.append(i)    
else:
    for j in range(Num1+1, Num2, 2):
        L1.append(j)


for i in range(Num1, Num2,2):
    L1.append(i)
    
print(L1)


# 23


L1 = []
L2 = []

for i in range(0, 10):
    L1.append(int(input("Enter Num for list 1 :")))
    
for j in range(0, 10):
    L2.append(int(input("Enter Num for list 2: ")))

L3 = L1+L2

def sort(get_list):
    for i in range(1, len(get_list)):
        if(get_list[i]<get_list[i-1]):
            j = i 
            while L3[j] < get_list[j-1] and j>0:
                get_list[j],get_list[j-1] = get_list[j-1], get_list[j]
                j = j-1
    return get_list

print(sort(L3))







