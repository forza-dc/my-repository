# names = ["Ahmed", "Aisha", "Adam", "Joseph", "Gabriel"]

# for name in names:
#     print(f"Hello {name}!")

# for i in range(1, 11):
#     print(f"{i}**2 = {i**2}")

# for i in range(1, 11):
#     print("\n")
#     for k in range(1, 11):
#         print(f"{i} x {k} = {i * k}")
    
# word = "clarusway"
# new_word = ""
# count = 0
# while count < len(word):
#     new_word += word[count] + "-"
#     count += 1
# print(new_word.rstrip("-"))



# a = 0
# while a < len("True"):
#     print(1) 
#     a += 1  

# number = 0

# while number <= 6:
#     print(number)
#     number += 1
# print("Number is bigger than 6")

# my_list = ['a', ('b', 'c'), 'd', 'e', "f", "g"]

# a = 0

# while a < len(my_list):
#     print(f"square of {a} is : {a ** 2}")
#     a += 1

# age = input("Please enter your age: ")

# while age.isdigit():
#     print(f"Great you entered valid input: {age}")
#     age = input("Please enter your age: ")
# print("You entered invalid input!!")

# cevap = 9

# soru = "Aklımdan bir sayi tuttum, hadi bil!  "
# print("Let's play the guessing game!!!")

# while True: 
#     tahmin = int(input(soru))

#     if tahmin < cevap:
#         print("Little higher...")
#     elif tahmin > cevap:
#         print("Little lower...")
#     else:
#         print("Bildiniz!!!")
#         break

# word1 = len(input("First word: "))
# word2 = len(input("Second word: "))
# word3 = len(input("Third word: "))
# words = [word1, word2, word3]
# words.sort()
# print(words[-1])

# sentence = input("Give me a sentence: ")
# words = sentence.split()
# counter = 0
# longest = 0
# print(words)
# while counter < len(words):
#     if len(words[counter]) > longest:
#         longest = len(words[counter])
#     counter += 1
# print(f"the length of the longest word: {longest}")

# liste = [1,2,3,4,5]
# for i in liste:
#     print(i)

# seasons = ['spring', 'summer', 'autumn', 'winter']
# for i in seasons:
#     print(len(i)) 

# names = ["Jalal", "M.Osman", "Alpaslan", "Aleyna"]

# for i in names:
#     print(f"Hello, {i}!")

# liste= []

# for i in range(1, 6):
#     liste.append(i)
#     print(i)

# word = "clarusway"
# count = 0
# for i in word:
#     count += 1
#     if count < len(word):
#         i = i + "-"
#     print(i, end="")

# word = [5,7,2,6,7853,7467]

# for i in word:
#     print(i+1)
