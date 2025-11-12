#1
int_list = [10,20,30,40]  # გლობალური ცვლადი

def f(num):                                     # ფუნქცია, რომელიც ამატებს რიცხვს გლობალურ სიაში
    global int_list                                          # გლობალური ცვლადის განსაზღვრა
    int_list.append(num)


f(50)

print(int_list, '\n')                                # გამოსავალი: [10, 20, 30, 40, 50]


#2
def sum_of_list(numbers):
    return sum(numbers)

example_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]       # სიას ვაძლევთ პარამეტრად

print("რიცხვთა ჯამია:", sum_of_list(example_list), '\n')

#3
gl_str = "Global"           # გლობალური ცვლადი

def local_str():
    gl_str = "Local"  
    return gl_str

# ფუნქციის გამოძახება
result = local_str()

# შედეგების დაბეჭდვა
print("ფუნქციის შედეგი:", result)     # "Local"
print("გლობალური ცვლადი:", gl_str, '\n')    # "Global"

#4

def digit_sum(a):
    if a < 10:                                # თუ რიცხვი ერთნიშნაა, ვაბრუნებთ მას
        return a
    else:
        return a % 10 + digit_sum(a // 10)

result = digit_sum(int(input('შეიყვანეთ მრავალნიშნა რიცხვი:')))
print("ციფრთა ჯამია:", result, '\n')


#5

def str(b):
    if len(b) <=1 :
        return b 
    else:
        return b[-1] + str(b[:-1])                                       #[-1] - ბოლო სიმბოლო   [ :-1] - მოჭრა ბოლო სიმბოლომდე
    
print("შებრუნებული სტრიქონი:", str(input("შეიყვანეთ სტრიქონი: ")))
