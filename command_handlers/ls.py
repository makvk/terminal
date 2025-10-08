from command_handlers import Command
import zipfile
class Ls(Command):
    def __init__(self, current_path, vfs_name):
        super().__init__(current_path, vfs_name)
    
    def _get_child_dir(self, arg_path):
        child_dirs = set()
        try:
            curr_list_path = arg_path.split('/')
            curr_list_path = [p for p in curr_list_path if (p and (p != '.'))]
            
            for member in self.all_members:
                member_list_path = member.split('/') 
                
                member_list_path = [p for p in member_list_path if (p and (p != '.'))][1:]

                if len(member_list_path) > len(curr_list_path):
                    if member_list_path[:len(curr_list_path)] == curr_list_path:
                        child_name = member_list_path[len(curr_list_path)]
                        if member_list_path[-1] == child_name:
                            if zipfile.ZipInfo(member).is_dir():
                                child_dirs.add('📁' + child_name)
                            else:
                                child_dirs.add('📄' + child_name)
                        
            return child_dirs
        except Exception as e:
            print(f"Error reading tar file: {e}")

    def handle(self, args = []):
        if len(args) == 0:
            print('\t', *self._get_child_dir(self.current_path))
        else: 
            arg = args[0]
            print('\t', *self._get_child_dir(self.current_path + '/' + arg.strip('/')))
            
        return self.current_path
