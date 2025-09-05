import os

VFS = r"C:\terminal"

while True:
    cmd_input = input(VFS + "> ")
    command = cmd_input.split()[0]
    args = cmd_input.split()
    args.pop(0)
    for i, arg in enumerate(args):
        if arg[0] == "$":
            args[i] = os.environ.get(arg[1:])

    if command[0] == "$":
        try:
            print(os.environ.get(command[1:]), sep = "\n")
        except:
            print("again")
    elif command == "ls":
        print(command, "\n", *args)
    elif command == "cd":
        print(command, "\n", *args)
    elif command == "exit":
        print("пока")
        break
    else: 
        print("unknown command")