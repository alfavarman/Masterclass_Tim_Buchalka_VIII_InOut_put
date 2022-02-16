# with open("set_summary.txt", "r") as source:
#     line = source.readlines()
#     print(line)
#     with open("new_file.txt", "w") as output:
#         print(line, end='', file=output)
#
# object_1 = "this is insert as a text", "this is insert as string, as well ", (
#     (0, "cannon"), (1, "bullet"), (4, "live"))
#
# with open('io_02_easy_to_write_hard_to_read.txt', 'w') as example:
#     print(object_1, end='', file=example)

with open('io_02_easy_to_write_hard_to_read.txt', 'r') as content:
    read_content = content.readline()

variable_for_objects = eval(read_content)
print(variable_for_objects)
a, b, c = variable_for_objects
print(a)
print(b)
print(c)

# For Security Sake it is not resonable to use Eval!
# as external file may be changed and include vunerable instructions,
# which program will execute.
