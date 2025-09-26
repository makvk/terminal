import tarfile
from command_handlers import Command

class Ls(Command):
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

    def handle(self, args = []):
        print(self._get_child_dir())
        return self.current_path
