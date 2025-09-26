from command_handlers import Command
import tarfile

class Cd(Command):
    def __init__(self, current_path, vfs_name):
        super().__init__(current_path, vfs_name)

    def _get_child_dir(self):
        child_dirs = set()
        try:
            tar = tarfile.open("./vfs/disk.tar")
            for member in tar.getmembers():
                member_list_path = member.name.split('/')
                curr_list_path = self.current_path.split('/')
                
                member_list_path = [p for p in member_list_path if (p and (p != '.'))]
                curr_list_path = [p for p in curr_list_path if p]

                if len(member_list_path) > len(curr_list_path):
                    if member_list_path[:len(curr_list_path)] == curr_list_path:
                        child_name = member_list_path[len(curr_list_path)]
                        child_dirs.add(child_name)
            
            tar.close()
        except Exception as e:
            print(f"Error reading tar file: {e}")
        
        return child_dirs

    def _one_dir_back(self):
        list_curr_path = (self.current_path).split('/')
        return '/'.join(list_curr_path[:-1])

    def handle(self, args = []):
        arg = args[0] if len(args) != 0 else ''
        if arg in self._get_child_dir():
            self.current_path += ('/' + arg)
        elif arg == "..":
            self.current_path = self._one_dir_back()
        elif arg == '.' or arg == '':
            return self.current_path
        else: 
            print("incorrect path")
        return self.current_path