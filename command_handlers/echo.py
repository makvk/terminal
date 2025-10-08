from command_handlers import Command

class Echo(Command):
    def __init__(self, current_path, vfs_name):
        super().__init__(current_path, vfs_name)

    def handle(self, args = []):
        print(*args)
        return self.current_path