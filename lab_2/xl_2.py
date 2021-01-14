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
from SROM_LAB_1 import power_mod
from SROM_LAB_1 import minus_mod
from SROM_LAB_1 import multy_mod
from SROM_LAB_1 import sqr_mod

##print("Введіть A")
##A = input().lower()
##print("Введіть B")
##B = input().lower()
##print("Введіть M")
##M = input().lower()
##A = HEX(A)
##B = HEX(B)
##M = HEX(M)

##line_prt()
##print("НСД")
##C = evklid(A.copy(),B.copy())
##print(turn(C))
##line_prt()
##line_prt()
##print("НСК")
##C = ICM(A.copy(),B.copy())
##ans = turn(C)
##print(ans)


A = HEX("4d3c91c579c2c6216567a5241614b561addf76c4bb659e6fe7f65ff76a918c843f0458b3ef457bcd9022d78798a29462ec99c74e6674690267d3e9844251b39d".lower())
B = HEX("af1abda4ad4d9fe3e36a529210c2ae99b905922fc0519798a26e351fe23af375ad6ba288ee030b70df0ce1cdf1e8b75ba56494dc6ed36b181814cd5783e6c8".lower())
M = HEX("b3786d3a85e62ec763a05a73a7f08d21eee3cbcae207e40854121bff8258f7b2b293b0d30277cdb987a6fcb5bf28b68d8e68aba88ded37bd80a879a1bb53e3".lower())

line_prt()
line_prt()
print("Плюс модуль")
K = plus_mod(A.copy(),B.copy(),M.copy())
ans = turn(K)
print(ans)
print(ans == "1a7526be614578d518883e82542ade9103b6f9f3248427e424f408c0ef34113943baaafa218ca58f307cd698b1d5f2e77fc9752d5961425522f194799c3af8")
line_prt()
line_prt()
print("Мінус модуль")
K = minus_mod(A.copy(),B.copy(),M.copy())
ans = turn(K)
print(ans)
print(ans == "233085ea1276969c18f44e4582869ba16f736d2967f0c0c3883bd6802f7019b34e0ac78e4a762a2081b10c684c55f14b51d1a2c59794db9ff418ed0e0b152e")
line_prt()
line_prt()

print("Помножити модуль")
K = multy_mod(A.copy(),B.copy(),M.copy())
ans = turn(K)
print(turn(Mod(multy(A,B),M)))
print(turn(Mod(multy(A,B),M)) == "ae616b17bdf4fac01e058450ff1ea598957f7977c184020e0649980f37754262744f18b47fa828c7d52228587ce7d3332b2fc312a9e2c6f15eff0e576b1eeb")
line_prt()
line_prt()

print("Квадрат модуль")
K = sqr_mod(A.copy(),B.copy(),M.copy())
ans = turn(K)
print(ans == "2de363147724bd08b8db8fb3633b75cb8c1139ba6daeb23152858038e07334eef4a1e7d140edb5fa6077291ac2669df86e5975d58f207dff7696db355fd779")
line_prt()
line_prt()
A = HEX("abcedefbcd")
B = HEX("abcde34")
M = HEX("ab")
print("Степінь")
K = power_mod(A,B,M)
ans = turn(K)
print(ans)
print(ans == "13")
line_prt()
line_prt()

