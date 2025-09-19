import os
import sys

script_args = sys.argv[1:]
is_script = False
script_errors = []

print("Имя скрипта:", sys.argv[0])
print("Переданные аргументы:", *script_args)

script_content = []
script_index = 0

for arg in script_args[1:]:
    f = open(arg, 'r')
    if f:
        for s in f.readlines():
            script_content.append(s.strip())
    

if len(script_content) != 0:
    is_script = True

print(script_content)

VFS = (os.path.basename(script_args[0]) + os.path.dirname(__file__)) if len(script_args) != 0 \
    else os.path.dirname(__file__) 

while True:
    try:
        if script_index < len(script_content):
            cmd_input = script_content[script_index]
            print(VFS + "> ", cmd_input)
            script_index+=1
        else:
            
            cmd_input = input(VFS + "> ")

        real_command_args = []
        list_command_args = cmd_input.split()

        for i, item in enumerate(list_command_args):
            if item[0] == "$":
                if os.environ.get(item[1:]) != None:
                    real_command_args.extend(os.environ.get(item[1:]).split())
                
            else:
                real_command_args.append(item)
        #        list_command_args[i] = os.environ.get(item[1:])

        if len(real_command_args) == 0:
            continue
        command = real_command_args[0]
        args = real_command_args[1:]
        
        if command == "ls":
            print(command, "\n", *args)
        elif command == "cd":
            print(command, "\n", *args)
        elif command == "exit":
            print("bye")
            break
        else: 
            if is_script:
                script_errors.append(script_content[script_index - 1])
                continue
            print(f"unknown command: {command}")
        if is_script:
            if script_index == len(script_content):
                is_script = False
                if len(script_errors) > 0:
                    print(f"errors in script: {script_errors}")
                continue
    except Exception as e:
        print(f"error: {e}")
