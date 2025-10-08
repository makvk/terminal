from command_handlers import Command
import getpass

class Whoami(Command):
    def __init__(self, current_path, vfs_name):
        super().__init__(current_path, vfs_name)

    def handle(self, args = []):
        print(getpass.getuser())
        
        return self.current_path