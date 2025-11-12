def flatten(arg): 
    for item in arg: 
        if isinstance(item, (list, tuple, set, frozenset)): 
            yield from flatten(item) 
        else: 
            yield item 



# ==========================
arr = [1, 2, 3, [[4, 5, 6], "Text", 7], {'title': 'The wolf', 'pages': 256}, (8, [9, 0], True, {5, 8, False})] 
arr = list(flatten(arr)) 
print(arr)


# def flatten(arg):
#     if isinstance(arg, dict):        
#         for value in arg.values():
#             yield from flatten(value)
#     elif isinstance(arg, (list, tuple, set, frozenset)):
#         for item in arg:
#             yield from flatten(item)
#     else:
#         yield arg



# # ==========================
# arr = [1, 2, 3, [[4, 5, 6], "Text", 7], {'title': 'The wolf', 'pages': 256}, (8, [9, 0], True, {5, 8, False})] 

# print(list(flatten(arr)))

