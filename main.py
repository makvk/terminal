import os
import sys
import tarfile
from command_handlers import commands

def main():
    tar = tarfile.open("./vfs/disk.tar")
    for member in tar:
        print(member.path)

    tar.close()
    
    shell_string = sys.argv

    cmd_name = shell_string[0]
    vfs_name = shell_string[1]
    script_args = shell_string[2:]

    print("Имя скрипта:", cmd_name)
    print("Имя VFS:", vfs_name)
    print("Переданные аргументы:", *script_args)

    # for arg in script_args[1:]:
    #     f = open(arg, 'r')
    #     if f:
    #         for s in f.readlines():
    #             script_content.append(s.strip())
        

    # if len(script_content) != 0:
    #     is_script = True

    # print(script_content)

    VFS = (os.path.basename(vfs_name) + os.path.dirname(__file__))
    
    current_path = '/home'

    while True:
        try:

            # if script_index < len(script_content):
            #     cmd_input = script_content[script_index]
            #     print(VFS + "> ", cmd_input)
            #     script_index += 1
            # else:
            cmd_input = input(vfs_name + current_path + "> ")

            real_command_args = []
            list_command_args = cmd_input.split()

            for i, item in enumerate(list_command_args):
                if item[0] == "$":
                    varname = item[1:]
                    if os.environ.get(varname) != None:
                        real_command_args.extend(os.environ.get(varname).split())     
                    else:
                        real_command_args.append(item)
                        list_command_args[i] = os.environ.get(varname)
                else: 
                    real_command_args.append(item)

            if len(real_command_args) == 0:
                continue

            command = real_command_args[0]
            args = real_command_args[1:]
            
            if command in commands:
                current_path = commands[command](current_path, vfs_name).handle(args)
            else: 
                print(f"unknown cmd: {command}")
            
        except Exception as e:
            print(f"error: {e}")

if __name__ == "__main__":
    main()