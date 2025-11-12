#1

x = int(eval(input("Enter a number:")))
arr = [44, 23, 11, 8, 20, 56, 33, 55]
if x in arr:
  print("The number in list")
else:
  print("The number not in list")


#2

a = int(eval(input("Enter an integer:")))
if (a % 2 == 1):
  print('The number is odd')
else:
  print('The number is even')


#3

st1 = input('შეიყვანეთ ტექსტი:')
st2 = input('შეიყვანეთ ტექსტი:')
if st1 is st2:
  print('Same object')
else:
  print("Different object")


#4

b = int(eval(input("Enter a number:")))
arr1 = [44, 23, 11, 8, 20, 56, 33, 55]
if b > arr[2] and b < arr[-1]:
  print('More than list elements')
elif b == arr[5]:
  print('Equal')
else:
  print("None of the conditions were met")