import os
import sys

print("Имя скрипта:", sys.argv[0])
print("Переданные аргументы:", *sys.argv[1:])

VFS = (os.path.basename(sys.argv[1]) + os.path.dirname(__file__)) if len(sys.argv[1:]) != 0 \
    else os.path.dirname(__file__) 

while True:
    try:
        cmd_input = input(VFS + "> ")
        command = cmd_input.split()[0]
        args = cmd_input.split()[1:]
        
        for i, arg in enumerate(args):
            if arg[0] == "$":
                args[i] = os.environ.get(arg[1:])

        if command[0] == "$":
                print(os.environ.get(command[1:]), sep = "\n", end = ': ')
        if command == "ls":
            print(command, "\n", *args)
        elif command == "cd":
            print(command, "\n", *args)
        elif command == "exit":
            print("bye")
            break
        else: 
            print("unknown command")
    except Exception as e:
        print(f"error: {e}")


