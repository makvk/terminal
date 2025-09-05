import os

VFS = r"C:\terminal"

while True:
    cmd_input = input(VFS + "> ")
    command = cmd_input.split()[0]
    args = cmd_input.split()[1:]
    
    for i, arg in enumerate(args):
        if arg[0] == "$":
            args[i] = os.environ.get(arg[1:])

    if command[0] == "$":
            print(os.environ.get(command[1:]), sep = "\n")
    elif command == "ls":
        print(command, "\n", *args)
    elif command == "cd":
        print(command, "\n", *args)
    elif command == "exit":
        print("bye")
        break
    else: 
        print("unknown command")