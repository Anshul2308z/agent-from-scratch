from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

result = get_file_content("calculator", "main.py")
print(result)

result = get_file_content("calculator", "pkg/calculator.py")
print(result)


result = get_file_content("calculator", "/bin/cat")
print(result)

result= get_file_content("calculator", "pkg/does_not_exist.py")
print(result)














# Debugging (T T)
#            (^)
# import os 
# a = os.path.abspath("calculator")
# print(a)
# b = target_file = os.path.normpath(
#     os.path.join(
#         a, "lorem.txt"
#     )
# )
# print ( b )
# print (
#     os.path.commonpath(
#         [a, b ]
#     )
# )
# with open( b, "r") as f:
#     c = f.read(20)
# print (c )