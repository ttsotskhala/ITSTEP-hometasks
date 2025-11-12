#1
data1 = input("შეიყვანეთ მონაცემები: ")
unique_set = set(data1.split())
print(unique_set)


#2
data2 = input("შეიყვანეთ მონაცემები: ")
unique_frozenset = frozenset(data2.split())
print("უცვლელი მონაცემები:", unique_frozenset)

#3
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_tuple = tuple(set1.union(set2))
print(union_tuple, "\n")


#4
data3 = input("შეიყვანეთ რიცხვების კორტეჟი (მაგ: 1, 2, 3, 2): ")
nums = data3.split()
input_tuple = tuple(int(e.strip()) for e in nums)                  # num_tuple = tuple(map(int, data3.split()))  როცა ვეძებდი სიაში სტრინგების რიცხვებად გადაკეთებას ამას წავაწყდი. ალბათ მოგვიანებით ვისწავლით უფრო დაწვრილებით
unique_list = list(set(input_tuple))
print(unique_list)


#5
people = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

for name, age in people:
    print(f"Name: {name}, Age: {age}")

#6
users1 = ["Irakli", "Giorgi", "Nona", "Oto"]
users2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
print("თანხვედრა:", list(set(users1).intersection(set(users2))))      # list(set(users1) & set(users2)) 