#1
# def fibonacci_list(n):
#     sequence = []
#     a, b = 0, 1
#     for _ in range(n):
#         sequence.append(a)
#         a, b = b, a + b
#     return sequence
# print(fibonacci_list(8))

#2
# def are_anagrams(str1, str2):
#     cleaned_str1 = str1.replace(" ", "").lower()      # ვაცლით სტრიქონებს ცარიელ ადგილებს და ვცვლით ასოების რეგისტრს
#     cleaned_str2 = str2.replace(" ", "").lower()
    
    
#     return sorted(cleaned_str1) == sorted(cleaned_str2)   #ვადარებთ
# print(are_anagrams("race", "care"))       # True
# print(are_anagrams("trap", "Part"))       # True
# print(are_anagrams("Judo", "shido"))      # False

#3
# def factorial(n):
#     if n < 0:
#         return "ფაქტორიალი უარყოფითი რიცხვებისთვის არ განისაზღვრება"
    
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result
# print(factorial(0))
# print(factorial(4))

#4
def count_character(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

print(count_character("Wonderful word", "r"))