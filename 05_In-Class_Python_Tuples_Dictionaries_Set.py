# my_tuple = ("wakabayashi",)
# my_tuple2 = "wakabayashi"
# my_tuple2 = tuple("wakabayashi")
# print(my_tuple, type(my_tuple), sep="\n")
# print(my_tuple2)

my_tuple = (1, 2, 3, 4, 564, 7, 863)
# my_list = list(my_tuple)
# my_tuple = [my_list]

# print(my_tuple, type(my_tuple), sep="\n")
# print(my_list, type(my_list), sep="\n")
# my_list[4] = 5
# my_tuple[5] = 5
# print(my_tuple)
# print(my_list)

# sehirler = ["Istanbul", "Izmir", "Ankara", "Van", "Erzurum", "Sivas", "Gonya", "Ssinop", "Mugla", "Gaziantep"]
# print(sehirler)
# sehirler_tuple = tuple(sehirler)

# sehirler[9] = "Yozgat"
# print(sehirler)
# sehirler_tuple[0] = "Mus"  # Bu çalışmaz.

# first_dict = {"kola" : 25, "ekmek" : 5, "makarna" : 5}
# second_dict = dict(kola=25, ekmek=5, makarna=5)

# state_capitals = {  "Arkansas" : "Little Rock", 
#                     "Colorado" : "Denver",
#                     "California" : "Sacramento",
#                     "Georgia" : "Atlanta"
# }

# # state_capitals = ["Virginia2" : "Richmond"]
# state_capitals["Virgina"] = "richmond"
# state_capitals["Virgina"] = "Richmond"
# print(state_capitals)

mix_values = {"animal" : ("dog", "cat"),  # tuple
                "planet" : ["Neptun", "Pluton", "Jupyter"],  # liste
                "number" : 40,  # integer
                "pi" : 3.14,  # float
                "is_good" : False  # boolean
}

mix_keys = {22 : "number",
            3.14 : "float",
            True : "boolean",
            "key" : "string"
}
# my_dictionary = dict(animal =("dog", "cat"), planet = ["Neptun", "Pluton", "Saturn"], number = 55)

# print(mix_values.items(), "\n")
# print(mix_keys.keys(), "\n")
# print(mix_values.values(), "\n")
# mix_values.update({"is_bad" : True})
# print(mix_values)

# del mix_values["is_bad"]
# print(mix_values)

# school_records={
# 	'personal_info':
# 		{'kid':{'tom':{'class':'intermediate', 'age':10},
# 			'sue':{'class':'elemantary', 'age':8}
# 			},
# 		'teen':{'joseph':{'class':'college', 'age':19},
# 			'marry':{'class':'high school', 'age':16}
# 			},
# 		},
#     'grades_info':
# 		{'kid':{'tom':{'math':88, 'speech':69},
# 			'sue':{'math':90, 'speech':81}

# 			},
# 		'teen':{'joseph':{'coding':80, 'math':89},
# 			'marry':{'coding':70, 'math':96}
# 			},
# 		}
# }



# print(school_records["grades_info"]["kid"]["sue"]["speech"])

# family = {
#     "erkek" : {
#         "baba" : {"yas" : 40, "meslek" : "eyt emeklisi" },
#         "kardes" : {"yas" : 22, "meslek" : "ogrenci"}
#     },
#     "kadin" : {
#         "anne" : {"yas" : 40, "meslek" : "emekli albay"},
#         "abla" : {"yas" : 27, "meslek" : "influencer"}
#     }
# }

# print(family["kadin"]["anne"]["meslek"])

# set_1 = {'red', 'blue', 'pink', 'red'}
# colors = 'red', 'blue', 'pink', 'red'
# set_2 = set(colors)
# print(type(set_1))
# print(set_2)
# bos_set = {}

# flower_list = ["rose", "orchid", "cactus", "violet", "ginger", "rose", "orchid", "tulip", "tulip"]
# flower_set = set(flower_list)

# print(flower_list)
# print(flower_set)

a = set("Ankara")
b = set("Istanbul")
c = set("Izmir")
d = set("Afyonkarahisar")
# print(a, b, c, d, sep= "\n")

# print(a.difference(b))  # == print(a - b)
# print(b.difference(a))  # == print(b - a)
# print(a.union(b))  # == print(a | b)
# print(b.union(a))  # == print(b | a)
# print(a.intersection(b))  # == print(a & b)

