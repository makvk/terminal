import abc
import zipfile

class Command(abc.ABC):
    def __init__(self, current_path, vfs_name):
        self.current_path = current_path
        self.vfs_name = vfs_name

        zip = zipfile.ZipFile(vfs_name)
        self.all_members = zip.namelist()
        zip.close()

    @abc.abstractmethod
    def handle(self, args = []):
        return self.current_path


        


