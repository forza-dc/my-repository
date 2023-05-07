# print('Here we go!')
# print('I will be the second text')
# a = '3'
# b = 5
# print('It is time for an error message :(')
# print(a + b)  # it won't be printed
# print("Sorry, but I won't be printed")  # it won't be printed

# while True:
#     try:
#         no_one = int(input("The first number please : "))
#         no_two = int(input("The second number please : "))
#         division = no_one / no_two
#         print("The result of the division is : ", division)
#         break
#     except ZeroDivisionError:
#         print("You can't divide by zero!. Try again.")
#     except ValueError:
#         print("Enter appropriate value.")




# print("Don't say I never make a mistake"

# print("""Don't say I never make a mistake")

# pirnt("Don't say I never make a mistake")

# x = 16

# for i in range (14, X):
#     print("hi")

# if 1 > 0 :
# print("hi")

# status = []

# if status:
#     print("''Hello universe")
# else
#     print("Hello universe'")

# x = ["1", "2", "3"]
# y = ["USA", "Japan", "Spain"]

# for i in y:
#     for j in X:
#         print(type([tuple(i+j)])) 

# print("Here we go")
# print("I will be the second text")
# a = "3"
# b = 5

# print("It's time for an error message :(")
# print(b + a)
# print("Sorry, but i won't be printed.")

# for i in range("x"):
#     print(i)

# print("2" + 2)


# while True:
#     try:
#         number1 = int(input("Enter a first number: "))
#         number2 = int(input("Enter a second number: "))
#         division = number1 / number2
#         print(f"The result is: {division}")
#         break
#     except TypeError:
#         print("You can't divide by zero.")
#     except ZeroDivisionError:
#         print("You cant divide by zero!")
#     except ValueError:
#         print("Hebele Hubele")
#     except: 
#         print("Hocam bunu ben bile bilemedim.")


# try:
#     file = open("my_file.txt", "r")
#     print(file.read())
# except:
#     print('There is no file named "my_file.txt"')

# while True:
#     try:
#         number1 = int(input("Enter a first number: "))
#         number2 = int(input("Enter a second number: "))
#         division = number1 / number2
#     except Exception as e:
#         print("Something went wrong.")
#         print(f"Probably it is because of {e}")
#     except ValueError:
#         print("You need to write appropriate value.")
#     else:
#         print(f"The result is: {division}")
#     finally:
#         print("It's done!")
#         break

# try:
#     x = 2 / 0
# except ZeroDivisionError:
#     print("You cant divide by zero!")
# except:
#     print("Something went wrong.")

# fruits = ['banana', 'mango', 'pear', 'apple', 'kiwi', 'grape']
# while True :
#     try :
#         a = fruits.index(100)
#         print(a)
#     except :
#         print('Calm down buddy')
#         break

fruits = ["banana", "mango", "pear", "apple", "kiwi", "grape"]

x = int(input("Please enter an index number to choose a fruit from the list: "))

while True:
    try:
        print(f"Your favorite fruit is {fruits[x]}.")
    except IndexError:
        print("Please enter a valid number between 0-5(including0).")
    except :
        print("Unknown error, please report to the coding man!") 
    finally:
        print("Thank you for trying our fruits!")
        break
