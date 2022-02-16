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

with open("set_summary.txt", "r") as source:
    for line in source:                     # with method close object automaticly
        print(line, end='')                 # once it's not needed
