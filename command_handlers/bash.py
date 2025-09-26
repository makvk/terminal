from command_handlers import Command

class Bash(Command):
    def __init__(self, script_args):
        super().__init__()
        self.script_index = -1
        self.script_content = []
        self.script_errors = set()

    def handle(self, args = []):
        print(args)
        return self.current_path