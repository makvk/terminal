from command_handlers import Command

class Uniq(Command):
    def __init__(self, current_path, vfs_name):
        super().__init__(current_path, vfs_name)

    def handle(self, args = []):
        print(*set(args))

        return self.current_path