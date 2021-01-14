from SROM_LAB_1 import HEX
from SROM_LAB_1 import plus
from SROM_LAB_1 import turn
from SROM_LAB_1 import minus
from SROM_LAB_1 import multy
from SROM_LAB_1 import power
from SROM_LAB_1 import squer
from SROM_LAB_1 import DivMod
from SROM_LAB_1 import Mod
from SROM_LAB_1 import line_prt
from SROM_LAB_1 import sr
from SROM_LAB_1 import equal
from SROM_LAB_1 import evklid
from SROM_LAB_1 import ICM
from SROM_LAB_1 import baret
from SROM_LAB_1 import plus_mod
#b = input()
ans = ""
'''
print("Введіть A")
A = input().lower()
print("Введіть B")
B = input().lower()
#print("Введіть M")
#M = input().lower()
A = HEX(A)
B = HEX(B)
#M = HEX(M)
line_prt()
print("Додавання")
C = plus(A,B)
print(turn(C))
line_prt()
line_prt()
print("Віднімання")
C = minus(A,B)
ans = turn(C)
print(ans)
line_prt()
line_prt()
print("Множення")
K = multy(A,B)
ans = turn(K)
print(ans)
line_prt()
line_prt()
'''
# Окремо степінь
print("Введіть A")
A = input().lower()
print("Введіть B")
B = input().lower()
A = HEX(A)
B = HEX(B)
D = power(A,B)
line_prt()
print("Степінь")
print(turn(D))
print("2e48a7109dda0748d2cb7898703429fa752cf89e24b8da05be44f475e82a7b92f00afa5a42ffcddbae04214e830dbd01b866b4a773cfc1a1ed7c196b1e118a76f34957dd1314150bf2bf62c26e230ea51eb28ffe7c6affd63d74b7bab0bd3278b49531fae77fac0755f7b7aefc9ef81a1290f91b89e5beb221fb0f7852f084f8e6513863b06b3f3b22fa1fb02da8e4e086e2597a934a1e40dcd3e3984380d3d927947ef66d09574e44e1bdce66405f3fc2b3968392057d108fcbc7ebfbae62bd25ecfe74a319f4b5b23c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000"==turn(D))


