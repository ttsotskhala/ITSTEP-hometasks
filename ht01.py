#1

a = eval(input("შეიყვენეთ რიცხვი 1:"))
b = eval(input("შეიყვენეთ რიცხვი 2:"))
print(a + b)
print(a - b)
print(a*b)
print(a/b)
print(a//b)
print(a % b)
print(a**b)


#2

d1 = eval(input("შეიყვენეთ პირველი დიაგონალის სიგრძე:"))
d2 = eval(input("შეიყვენეთ მეორე დიაგონალის სიგრძე:"))
S1 = d1*d2/2
print(f"რომბის ფართობი - {S1}")

#3

l = eval(input("შეიყვანეთ მეტრების რაოდენობა"))
print(f"{l*100} სმ")
print(f"{l*10} დმ")
print (f"{l*1000} მმ")
print(f"{l/1609.344} მილი")


#4

h = eval(input("შეიყვენეთ სამკუთხედის სიმაღლე:"))
c = eval(input("შეიყვენეთ სამკუთხედის ფუძე:"))
S2 = h*c/2
print(f"სამკუთხედის ფართობი - {S2}")


#5

two_digit_number = eval(input("შეიყვანეთ ორნიშნა რიცხვი:"))
num_str = str(two_digit_number)
dig1 = int(num_str[0])
dig2 = int(num_str[1])
dig_sum = dig1 + dig2
print(f'ორნიშნა რიცხვი {two_digit_number}-ის/ს ციფრთა ჯამი არის {dig_sum}')