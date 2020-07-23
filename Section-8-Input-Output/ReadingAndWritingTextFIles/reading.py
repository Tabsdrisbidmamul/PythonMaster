# file = open("sample.txt", "r")
#
# for line in file:
#     if "jabberwock" in line.casefold():
#         print(line, end="")
#
# file.close()

# with open("sample.txt", "r") as file_obj:
#     for line in file_obj:
#         if "jabberwock" in line.lower():
#             print(line, end="")

# with open("sample.txt", "r") as file:
#     line = file.readline()
#     while line:
#         print(line, end="")
#         line = file.readline()

# with open("sample.txt", "r") as file:
#     # returns a list of lines
#     lines = file.readlines()
#     print(lines)
#
#     for line in lines:
#         print(line, end="")

with open("sample.txt", "r") as file:
    # returns a list of lines
    lines = file.read()
    # print(lines)

    for line in lines[::-1]:
        print(line, end="")
