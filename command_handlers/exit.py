from command_handlers import Command

class Exit(Command):
    def handle(self, args = []): 
        exit(0)