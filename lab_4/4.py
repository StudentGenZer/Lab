from functools import reduce
 
 
M, P = 359, 359 * 2 + 1
 
def line_prt():
    print("=================================================================")
     
def cell(x, y):
    return (2**x + 2**y + P**M) % P == 1 \
        or (2**x - 2**y + P**M) % P == 1 \
        or (-2**x + 2**y + P**M) % P == 1 \
        or (-2**y - 2**x + P**M) % P == 1
 
 
matrix = [[int(cell(i, j)) for j in range(M)] for i in range(M)]
 
 
def bitand(a: list, b: list):
    a, b = fit(a, b)
    return [a[i] & b[i] for i in range(len(a))]
 
 
def shright(v: list):
    v.insert(0, v.pop())
 
 
def shleft(v: list):
    x = v.pop(0)
    v.append(x)
 
 
def nul():
    return [0] * M
 
 
def one():
    return [1] * M
 
 
def inv():
    return [1] * (M - 1) + [0]
 
 
def fit(x: list, y: list):
    return max(len(y) - len(x), 0) * [0] + x, max(len(x) - len(y), 0) * [0] + y
 
 
def log(b):
    return 1 not in b
 
 
def inp(s: str):
    temp = list(map(lambda j: int(j), filter(lambda i: i in '10', s)))
    return [0] * (M - len(temp)) + temp
 
 
def prt(x: list):
    return ''.join(map(lambda i: str(i), x))
 
 
def plus(a: list, b: list):
    a, b = fit(a, b)
    return [a[i] ^ b[i] for i in range(len(a))]
 
 
def sqr(a: list):
    v = a.copy()
    shright(v)
    return v
 
 
def power(a: list, b: list):
    return one() if log(b) else \
            multy(sqr(power(a, [0] + b[:-1])), a) if b[len(b) - 1] else sqr(power(a, [0] + b[:-1]))
 
 
def inverse(v: list):
    return power(v, inv())
 
 
def trace(v: list):
    return v.count(1) & 1
 
 
def multy(_a: list, _b: list):
    a = _a.copy()
    b = _b.copy()
    res, temp = nul(), nul()
    for i in range(M):
        for j in range(M):
            temp[j] = trace(bitand(matrix[j], a))
        res[i] = trace(bitand(temp, b))
        shleft(a)
        shleft(b)
    return res
 
a = inp("11001111000011010111111101101000111001101010001011000010010110110100100101101000001011101100101001100101101101011010101001100010011111100101000101100010101100100010100000011111110011100101110110111010101100111000100000000110100110010110111011011110101111011101110110001001101100001011101011100100001011100101101100000010110000011011101011101110010110010000110")


b = inp("10001001010111000100000001111100011100111111010110101011101100100011010010000001101011100100001111000110111010000101011101010011010001001101111011100001001001001110110110111011010100101111101000111000000011111010101110010101111011101100010010101010000011111011111101100111000000011011110010101000110111111101100101101110001010001110010110111110101110001011000")

n = inp("10010000100011001101100110010011010110010100001001000101010010111101000101111001101110011111011111101011011011011100011001000100100110100000101010000001101010000110010001110001100011011010100101011101010001001001001011001010011101001011000000110100111000001001011100111101000000011101100001101111101110110000110001001110101111100111000001111111100011110000000")



##print("a1",a)
##print("b1",b)


line_prt()
line_prt()
print("Додавання")
c = plus(a.copy(),b.copy())
print(prt(c))
print(prt(c) == "01000110010100010011111100010100100101010101011101101001111010010111110111101001100000001000100110100011010111011111110100110001001110101000111110000011100101101100010110100100100111001010011110000010101111000010001110010011011101111010101001110100101100100110001011101110101100010000011001001100111100011000001001101100111010010101111101010000111000011011110")
line_prt()
line_prt()
print("Множення")
d = multy(a.copy(),b.copy())
print(prt(d))
print(prt(d)=="00101101010100001000011011101110010001111110111110110110101100101111110101000100001001100111011111110110101010110000010010010001110011000001111111101111001000001111111110101101011110000111110010000000110000001111110111101010111001001101110011010001000110100010110110000000010010100000111000000001110100011000101111010101010010010101101110101001011011011101001")
line_prt()
line_prt()
print("Квадрат")
k = sqr(a)
print(prt(k))
print(prt(k)=="01100111100001101011111110110100011100110101000101100001001011011010010010110100000101110110010100110010110110101101010100110001001111110010100010110001010110010001010000001111111001110010111011011101010110011100010000000011010011001011011101101111010111101110111011000100110110000101110101110010000101110010110110000001011000001101110101110111001011001000011")
line_prt()
line_prt()
print("Степінь")
s = power(a.copy(), b.copy())
print(prt(s))
print(prt(s)=="10111000011010111100001010000111010010111101001010110001110001101000101001101001101011100111110101111010100001000110001010010110001010001111110010000000011100111000111000111111011000000110111010111010100101010001011100110101101010101110101100111110011110110011101001101110010101111010111000011111001010000011110110101001100100001011110100010000011000100100100")
line_prt()
line_prt()
print("Оберненого")
q = inverse(a.copy(), b.copy())
print(prt(q))
print(prt(q)=="01010001100000000001001101100100000111100111100110010101001100111111011000010000000010000001001110110011100111111111000100111011111101100111111101000000011011000111100011110001100001111101100000000010010010111001100111101011111100110101001101100100001100000100100011000001011010011111010100011010100110000101101011100011011000011001000001001100001010110010000")
line_prt()
line_prt()
print("Слід a")
f = trace(a.copy())
print(f)
print(f == 0)

