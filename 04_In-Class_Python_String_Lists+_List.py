# text = "www.clarusway.com"
# print(text.startswith("www"))
# print(text.endswith(".om"))

# game = "Witcher 3"
# print(game.endswith("4"))

# sentence = "I live and work in Turkey"

# sentence = sentence.capitalize()

# print("I live and work in Turkey".capitalize())
# print(sentence.capitalize())
# print(sentence.upper())
# print(sentence.lower())
# print(sentence.title())
# print(sentence.replace("Turkey", "Japan"))
# print(sentence.swapcase())
# text = "clarusway.com"
# print(text.replace("s", "m"))

# text2 = "mERHABA DÜNYALI BEN DOSTUM"

# print(text2.capitalize())
# print(text2.lower())
# print(text2.title())

# print(sentence)
# print(text)
# print(text2)

# cumle = "Pc her zaman console oyunlarini dover."

# print(cumle.upper())
# print(cumle)

# cumle = cumle.upper()

# print(cumle)

# print(cumle.upper().lower().capitalize().swapcase())

# print(cumle.replace("Pc", "Bilgisayar"))

# print(sentence.replace("i", "+"))

# print(sentence)


# text3 = "         listen first            "
# print("         listen first            ")
# print(text3.strip())

# space_string = "     listen first      "
# print(space_string.strip())  # removes all spaces from both sides

# source_string = "tyintertyoperabilityty"
# # removes trailing "y" or "i" or "yi" or "iy" from both sides
# print(source_string.strip("ty"))  

# space_string = "     listen first"
# print(space_string.lstrip())  # removes all spaces from left sides

# source_string = "tyinteroperability"
# # removes "i" or "n" or "in" or "ni" from the left side
# print(source_string.lstrip("ty"))  

# space_string = "     listen first      "
# print(space_string.rstrip())  # removes all spaces from right side

# source_string = "tyinteroperability"
# # removes "t" or "y" or "ty" or "yt" from the right side
# print(source_string.rstrip("ty")) 

# text = 'tyou can learn almost everything in pre-classz'

# print(text.lstrip("t").rstrip("z").upper())

# print(text.upper().strip("TZ"))

# text4 = ["Kuroko no Basket", 36, ["Slam Dunk"], 3.14]
# print(text4)

# list() []
# tuple() ()
# dict() {}
# set() 

# liste = ["happy", 36, 3.14, ["unhappy"]]
# liste2 = "happy"
# print(list(liste))
# print(list(liste2))
# print(liste2)

# country = ["USA", "New Zealand", "Finland", "Sweden", "Syria", "Turkey"]
# print(country)

# mixed_list = [11, "Joseph", False, 3.14, None, {1:"bir"}]
# print(mixed_list)
# print(type(None))

# mixed_list = [11, 'Joseph', False, 3.14, None, {1:"bir"}]
# output = list(mixed_list)
# print(output)

# my_list = ['Aslan', 'Clarusway', 2022]
# new_list1 = list(my_list)
# new_list2 = [my_list]
# print(new_list1)
# print(new_list2)
# print(len(new_list1))
# print(len(new_list2))

# empty_list = []
# empty_list.append(1)
# empty_list.append("Multiverse")
# empty_list.append("Multiuniverse")
# empty_list.append(3.14)
# empty_list.append([5])
# print(empty_list)

# city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney']
# city.append(‘Addis Ababa’)

# print(city)

# empty_list = []
# empty_list.append(1) 
# empty_list.append(2) 
# empty_list.append(3) 
# empty_list.append(4) 
# print(empty_list)

# liste4 = [1, 4, 7]
# liste4.insert(0, 5)
# liste4.insert(0, "string")
# print(liste4)

# liste4.pop()
# liste4.remove(5)
# print(liste4)

# print(ord("A"))
# print(ord("a"))

# liste6 = [3, 5, 1, 9, 0]
# liste6.sort()
# print(liste6)

# list_1 = ['one', 'four', 'nine']
# list_2 = ['@', '*-', 'False']
# list_3 = [True, False, None]
# list_4 = [[3], [44], [-12]]
# list_5 = [[1, 3], [44, -40], [-12, 1]]
# print(len(list_1))
# print(len(list_2))
# print(len(list_3))
# print(len(list_4))
# print(len(list_5))


# print(list_2)
# print(list_3)
# print(list_4)
# print(list_5)

# list_5 = [[1, 3], [44, -40], [-12, 1]]
# list5 = list5[1][0]

# print(list_5[1])
# print(list_5[1][0])

# [start:stop:step]

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[:])

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[3:])

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[:5])

# animals = ['elephant', 'bear', 'fox', 'wolf', 'rabbit', 'deer', 'giraffe']
# print(animals[::2])

# print(len(["Aslan", "Geralt", "Yenefer", ""][1]))

# flowers = [["jasmine", ["lavender", "rose"], "tulip"]]
# colors = ["red", ("blue", ["yellow", "green"]), "pink"]
# flowers[0][1].append("ginger")
# print(flowers)

# output = "My two favorite flowers are {} and {}, two favorite colors are {} and {}.".format(flowers[0][2], flowers[0][1][1], colors[1][0], colors[1][1][1])

# print(output)

# numbers2 = (list(range(11)[1:11:2]))
# print(f" These are our odd numbers :{numbers2}")

# my_abc = [1, 2, 3]
# ters_myabc = []
# sayac = len(my_abc)
# for i in range(len(my_abc)):
#     # print(i)
#     ters_myabc.append(my_abc[len(my_abc)-(i-1)])
#     # my_abc.remove(i-1)
# print(ters_myabc)

# while sayac != 0:
#     ters_myabc.append(my_abc[-1])
#     my_abc.pop(-1)
#     sayac -= 1
# print(ters_myabc)

# for i in range(1, len(my_abc)+1) :
#     # print(i)
#     ters_myabc.append(my_abc[len(my_abc)-i])
# print(ters_myabc)

# vize = input(' Vize Notu : ')
# final = input(' Final Notu : ')
# total = (float(vize)*0.3) + (float(final)*0.7)
# print("vize notum : {0}, final notum :{1} total :{2} ".format(vize, final, total))

# Score_letter = 20
# print ("Your degree: %c" % Score_letter)

# not1 = int(input("1.Sınav Notunu Giriniz: "))
# not2 = int(input("2.Sınav Notunu Giriniz: "))
# ortalama = int((not1+not2)/2)
# if (not1 and not2) > 100 and (not1 and not2) < 0:
#     pass
#     if ortalama > 0 and ortalama <45:
#         print("Sınıfta Kaldın", ortalama)
#     elif ortalama >45 and ortalama<70:
#         print("Herhangi Bir Belge Almadan Geçtin.", ortalama)
#     elif ortalama>69.99 and ortalama<85:
#         print("Teşekkür Belgesi ile Geçtin.", ortalama)
#     elif ortalama>84.99 and ortalama<100.1:
#         print("Takdir Belgesi ile Geçtin.", ortalama)
# print("Geçersiz Not Girdiniz")

# student_ages = {"Harry": 29,
#                 "Clark": 32,
#                 "Peter": 22,
#                 "Bruce": 36
#                 }

# print(student_ages["Bruce"])

# dict_by_dict = {'animal':'dog',
# 			'planet': 'Neptun',
# 			'number': 40,
# 			'pi':3.14,
# 			'is_good': True}

# print(dict_by_dict.items(), '\n')
# print(dict_by_dict.keys(), '\n')
# print(dict_by_dict.values(), '\n')
