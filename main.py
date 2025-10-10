import os
import sys
from command_handlers import commands

def main():
    shell_string = sys.argv

    cmd_name = shell_string[0]
    vfs_name = shell_string[1]
    script_args = shell_string[2:]

    print("Имя скрипта:", cmd_name)
    print("Имя VFS:", vfs_name)
    print("Переданные аргументы:", *script_args)

    script_content = []
    script_index = 0
    script_errors = []
    for arg in script_args:
        f = open(arg, 'r')
        if f:
            for s in f.readlines():
                script_content.append(s.strip())
        f.close()
        
    if len(script_content) != 0:
        is_script = True
    else: 
        is_script = False
    
    current_path = ""

    while True:
        try:
            vfs_invite = vfs_name.split('/')[-1]
            if script_index == len(script_content):
                is_script = False
                if len(script_errors) != 0:
                    print("errors in script: ", *script_errors)
                script_index += 1
                
            if script_index < len(script_content):
                cmd_input = script_content[script_index]
                print(vfs_invite + current_path + "> ", cmd_input)
                script_index += 1
            else:
                cmd_input = input(vfs_invite + current_path + "> ")

            real_command_args = []
            list_command_args = cmd_input.split()

            for item in list_command_args:
                if item[0] == "$":
                    varname = item[1:]
                    if os.environ.get(varname) != None:
                        real_command_args.extend(os.environ.get(varname).split())     
                    else:
                        real_command_args.append(item)
                else: 
                    real_command_args.append(item)

            if len(real_command_args) == 0:
                continue

            command = real_command_args[0]
            args = real_command_args[1:]
            
            if command in commands:
                current_path = commands[command](current_path, vfs_name).handle(args)
            else: 
                if is_script:
                    script_errors.append(command)
                else:
                    print(f"unknown cmd: {command}")

        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    main()