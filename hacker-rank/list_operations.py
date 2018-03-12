# Consider a list (list = []). You can perform the following commands:
#
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

no_of_commands = int(raw_input("Enter no of commands :"))

list = []

for _ in range(no_of_commands):
    cmd_str = raw_input()
    splitted_cmd = cmd_str.split()
    cmd = splitted_cmd[0]
    args = splitted_cmd[1:]
    if cmd != "print":
        cmd += "(" + ",".join(args) + ")"
        eval("list."+cmd)
    else:
        print list
