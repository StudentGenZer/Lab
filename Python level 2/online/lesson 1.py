string = "Hello"   
num = 10        
num_2 = 12.5
List = [1,2,3,4]

#print("Hello World")
#name = input("name: ")

#age = int(input("age: "))       # "15" -> 15
#power = float(input("power: ")) #  "36.5" -> 36.5
#num_str = str(1234)             # 1234 -> "1234"
#arr = list("Python")            # "Python" -> ["P","y","t","h","o","n"]

# >
# <
# ==
# !=
# >=
# <=
# or   - () or ()
# and  - () and ()
# not  - not(True) = False; not(False) = True

##print(5 > 10)
##print(10 != 9)
##print(not(7 == 7))


##a = 5
##if a > 18:
##    print("More")
##elif a == 18:
##    print("Eq")
##else:
##    print("Less")

# +
# -
# *
# /
# %
# //
# ** - степінь

'''
Високосний рік - це змінна year
Виводить True, якщо націло ділить на 4, при умові що він не ділиться на 100,
Якщо year націло дітись на 400, то також виводити True
Всі інші, виводити False.

2004 - True
2000 - True
1700 - False
1993 - False
1600 - True
2020 - True
'''


##year = int(input("Рік: "))
##
##if year % 4 == 0:
##    if (year % 100 == 0) and (year % 400 != 0):
##        print(False)
##    else:
##        print(True)
##else:
##    print(False)

'''
Вводиться число - num
Потрібно вивести True, якщо num попадає в інтервал від 5 до 15
5 < num < 15 - True

10 - True
0 - False
29 - False
15 - False
5 - False
'''

##num = int(input("num: "))
##if num > 5 and num < 15:
##    print(True)
##else:
##    print(False)


for i in range(0, 10):
    if i % 2 == 0:
        print(i)

for i in range(0,11):
    print(i*5)

for i in range(0,11):
    print("*"*20)











