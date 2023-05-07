# count = 0
# while count < 5:
#     print("Halil Pazarlama")
#     count += 1
# print("Osman Pazarlama")

# isim = "M.Osman"

# for i in isim:
#     print(i, end=" ")

# times = int(input("Kac defa seni seviyorum yazdirmaliyim?: "))
# count = 1
# while count <= times:
#     count += 1
#     print("Seni seviyorum")

# for i in range(times):
#     print("Seni seviyorum.")

# number = int(input("enter a number between 1-10: "))

# for i in range(11):
#     print(f"{number} x {i} = {number * i}")

# i=1
# sayi=int(input("Bir ile on arasında bir sayı giriniz: "))
# while i<=10:
#     if 1<=sayi<=10:
#         print(f"{sayi} x {i}= {sayi * i}")
#         i=i+1
#     else:
#         print("Yazdığınız sayıyı kontrol ediniz")
#         break

# b = list(range(10))
# print(b)

# a = set(b)
# print(a)
# c = "Havva Nur"
# c = set(c)
# print(c)

# print(range(5))
# print(*range(5))
# print(*range(5,22,2))
# print(*("seperate"))
# print(*(range(10,0,-2)))

# numbers = [0,1,2,3,4,5]
# text = ["zero", "one", "two","three", "four"]

# for x, y in zip(numbers, text):
#     print(x,":", y)

# evens = []
# odds = []
# for i in range(11):
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
# print(evens)
# print(odds)

# numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
# evens = []
# odds = []
# for i in numbers :
#     if i %2 == 0 :
#         evens.append(i)
#     else:
#         odds.append(i)
# print(f"The number of even numbers: {len(evens)}")
# print(f"The number of odd numbers: {len(odds)}")


# numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
# evens = 0
# odds = 0
# for i in numbers :
#     if i % 2 == 0 :
#         evens += 1
#     else:
#         odds += 1
# print(f"The number of even numbers: {evens}")
# print(f"The number of odd numbers: {odds}")

# for i in range(1, 10):
#     print(str(i) * i)

# for i in range(1, 10):
#     print(f"{i}" * i)

# toplam = 0

# for i in range(1, 75):
#     toplam += i
#     # print(toplam)
# print(toplam)

# who = ["I am ", "You are "]
# mood = ["happy", "confident"]

# for i in who:
#     for k in mood:
#         print(i+k)

# names = ["susan", "tom", "edward"] 
# mood = ["happy", "sad"]
# for i in names:
#     for k in mood:
#         print(f"{i.capitalize()} is {k}")

# for i in range(1, 11):
#     for k in range(1, 11):
#         print(f"{i} * {k} = {i * k}")
#     print("")

# for i in range(10): # piramit
#      print ((9-i) * f" " + (2*i-1)* f"{i}")

# for i in range(1, 7):
#     for k in range(i):
#         print("* ", end="")
#     print("")

# for i in range(7, 0, -1):
#     for k in range(i):
#         print("* ", end="")
#     print("")

# for i in range(9,0,-1): # ters yıldızlı piramit
#     print ((9-i) * f" " + (2*i-1)* "* ")

# n = 5
# for i in range(1, n):
#     print(" " * (n - i - 1) + "* " * (i + 1))
# for k in range(n-1, 0, -1):
#     print(" " * (n - k) + "* " * k)

# for k in range(9,1,-1):
#     print ((10-k) * " " + (2*k-1)* f"*")

# for i in range(10): # piramit
#     print ((10-i) * " " + (2*i-1)* f"*")

# n = int(input("Enter a number: "))

# if n > 0:
#     for i in range(2, n):
#       if n % i == 0:
#         print(f"{n} is not a prime number.")
#         break
#     else:
#       print(f'{n} is prime number.')
# else:
#     print('positive numbers only')