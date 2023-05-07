# def ilk_fonksiyonumuz(a, b):
#     print((a ** 2) + (b ** 2))

# ilk_fonksiyonumuz(2,3)

# a = 5
# b = 10

# ilk_fonksiyonumuz(a,b)

# def motto():
#     print("Get up, Stand up, Don't Give up the Fight!")
# motto()

# def topla(a,b):
#     print(a + b)

# topla(1,2)

# def calculator(a,b,c):
#     if c == "+":
#         print(f"{a}+{b}={a + b}")
#     elif c == "-" :
#         print(f"{a}-{b}={a - b}")
#     elif c == "*" :
#         print(f"{a}*{b}={a * b}")
#     elif c == "//" :
#         print(f"{a}/{b}={a // b}")
#     else:
#         print("Düzgün bir şey girer misin lütfen?")
        
# calculator(88,22,"a")

# def multiply(a, b):
#     print(a * b)

# multiply(2,3)

# def carpma(a, b):
#     return a * b
# print(carpma(2,3))

# print(type(multiply(2,3)))
# print(type(carpma(2,3)))

# def naber():
#     print("Nasilsin?")

# def iyiyim():
#     naber()
#     return "iyiyim senden naber?"

# print(iyiyim())

# def Rcalculator(a,b,r):
#     if r == "+":
#         return (a + b)
#     elif r == "-":
#         return (a - b)
#     elif r == "*":
#         return (a * b)
#     elif r == "/":
#         return (a / b)
#     else:
#         return "Duzgun bir operator giriniz"
# print(Rcalculator(22, 33, "a"))

# def absolute_value(num):
#     if num > 0:
#         return num
#     elif num == 0:
#         return "Sifir sifirdir."
#     else:
#         return -num
# print(absolute_value(0))

# def max_length():
#     l = []
#     k = []
#     for i in range(4):
#         kelime = input("lütfen bir kelime giriniz: ")
#         l.append(len(kelime))
#         k.append(kelime)
#     return (f"{k[l.index(max(l))]} kelimesi daha uzun bir kelimedir : {max(l)}")

# print(max_length())

def uzunu_bul():
    k = []
    l = []
    for i in range(4):
        kelime = input("4 Kelime giriniz:")
        k.append(kelime)
    # print(k)
    a = 0
    for i in k:
        if a < len(i):
            l.append(i)
            a = len(i)           
        # else:
        #     continue
    return f"{l[-1]} is the longest one."
print(uzunu_bul())