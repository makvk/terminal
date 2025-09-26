import abc

class Command(abc.ABC):
    def __init__(self, current_path, vfs_name):
        self.current_path = current_path
        self.vfs_name = vfs_name

    @abc.abstractmethod
    def handle(self, args = []):
        pass