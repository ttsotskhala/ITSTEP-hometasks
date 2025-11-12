#1.

n = int(eval(input("Enter an integer:")))

print(f"1-დან {n}-მდე რიცხვთა ჯამი ტოლია: {sum(range(1,n+1))}")

#ან
S=n*(n+1)//2
print(f"1-დან {n}-მდე რიცხვთა ჯამი ტოლია: {S}")

#2

i = int(eval(input("Enter an integer:")))

while i >= 1:
    print(i, end=", " if i > 1 else "")
    i -= 1

print()

#3
from random import randint

num = randint(1, 80)
i = 1
print("Was guessed a number between 1 and 80. Guess it...\n")

guess = 0
while guess != num:
  guess = int(eval(input(f"Step №{i}. Your guess: ")))
  if guess > num:
    print("Too great")
  elif guess < num:
    print("Too less")
  print()
  i += 1
else:
  print(f"You guessed a number! It is {num}.")

print("You're magnificent!\n")

# #4

total_sum = 0

while True:
    user_input = input("Enter an integer (or 'sum' to get the sum): ")

    if user_input.lower() == 'sum':
        print(f"Sum of the positive numbers is: {total_sum}")
        break 
    else:           
        number = int(user_input)           
        if number > 0:
            total_sum += number
