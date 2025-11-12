#1

my_list = []       # ცარიელი სია

while True:
    command = input("შეიყვანეთ ბრძანება (a - დამატება, r - წაშლა, e - გასვლა): ")

    if command == 'a':
        number = input("შეიყვანეთ რიცხვი დასამატებლად: ")
        my_list.append(number)
        print("განახლებული სია:", my_list)
    elif command == 'r':
        number = input("შეიყვანეთ რიცხვი წასაშლელად: ")
        number = (number)
        if number in my_list:
            my_list.remove(number)
            print("განახლებული სია:", my_list)
        else:
                print("ეს რიცხვი სიაში არ არის")
    elif command == 'e':
        print("პროგრამა დასრულდა.")
        break
    else:
        print("არასწორი ბრძანება. გამოიყენეთ a, r ან e.")






#2

my_list_1 = [43, '22', 12, 66, 210, ["hi"]]                       #საწყისი სია
#a.
index_210 = my_list_1.index(210)                                  #დაბეჭდავს 210-ის ინდექსს
print("a. 210-ის ინდექსია:", index_210)
# b.                                                              # დაამატებს ბოლო ელემენტში ტექსტს "hello"-ს
my_list_1[-1].append("hello")
print("b. სია 'hello'-ს დამატების შემდეგ:", my_list_1)

# c.                                                              # წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას
del my_list_1[2]
print("c. სია მასში მეორე ინდექსის წაშლის შემდეგ:", my_list_1)

# d. 
my_list_2 = my_list_1.copy()                                       # ახალი სიის (კოპიის) შექმნა
my_list_2.clear()                                                  # გასუფთავება
print("d. საწყისი სია:", my_list_1)
print("გასუფთავებული სია:", my_list_2)




#3

import re

phone = input("შეიყვანეთ ტელეფონის ნომერი ფორმატით (123) 456-789: ")

pattern = r"\(\d{3}\) \d{3}-\d{3}"                  

if re.fullmatch(pattern, phone):
    print("შეყვანილი ტელეფონის ნომერი სწორია:", phone)
else:
    print("Invalid format")