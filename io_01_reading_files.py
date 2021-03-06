# summary = open("set_summary.txt", "r")
#
# # for line in summary:
# #     print(line)
#
# for line in summary:
#     if "set" in line.lower():
#         print(line, end="")
#
# summary.close()

# with also handle error on objects, and close object before error terminates program
# with open("set_summary.txt", "r") as source:
#     for line in source:                     # with method close object automatically
#         print(line, end='')                 # once it's not needed
#
#
# with open("set_summary.txt", "r") as source:
#     line = source.readline()                # if file is empty it won't proceed to while loop
#     while line:
#         print(line, end='')
#         line = source.readline()


# with open("set_summary.txt", "r") as source:
#     lines = source.readlines()                # read all the lines, as a list
# print(lines, end='')                          # shows in each element \n which shows why
#                                               # use end=''
# for line in lines:
#     print(line, end='')

with open("set_summary.txt", "r") as source:
    lines = source.read()                       # `read` reads entire file
print(lines, end='')                            # overloading memory
for line in lines:
    print(line, end='')