# #1

# def zip_lists(list1, list2):
#     try:
#         if not isinstance(list1, list) or not isinstance(list2, list):
#               raise TypeError("ორივე პარამეტრი უნდა იყოს სია")
#         return [str(i) for i in zip(list1, list2)]
#     except TypeError as e:
#         print(f"TypeError: {e}")
#     except Exception as e:
#         print(f"Error: {e}")
# #=======================

# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# print(zip_lists(list1, list2))


# 2

# from functools import reduce

# def multiply_num(nums):
#     try:
#         return reduce(lambda x, y: x * y, nums)
#     except TypeError:
#         return "TypeError: შეიყვანეთ მხოლოდ რიცხვები"
    
# #===============

# print(multiply_num([1, 2, 3, 4, 5]))


# 3

# odds = lambda nums: [x for x in nums if x % 2 != 0]

# #====================

# nums = [1, 2, 3, 4, 5, 6, 7]
# print(odds(nums))  # [1, 3, 5, 7]


4

def ending_filter(words, ending):
    try:
        if not isinstance(words, list):
            raise TypeError("პირველი პარამეტრი უნდა იყოს სია")
        if not all(isinstance(word, str) for word in words):
            raise TypeError("სია უნდა შეიცავდეს მხოლოდ სტრიქონებს")
        if not isinstance(ending, str):
            raise TypeError("მეორე პარამეტრი უნდა იყოს სტრიქონი")

        return list(filter(lambda word: word.endswith(ending), words))
    
    except TypeError as ex:
        print(f"TypeError: {ex}")
    except NameError as ex:
        print(f"NameError: {ex}")
    except Exception as ex:
        print(f"Error: {ex}")


#=====================

print(ending_filter(['game', 'lame', 'play', 'kinder', 'aim'], 'ame'))