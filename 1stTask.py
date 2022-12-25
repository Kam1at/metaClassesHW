import os


class ChangeDir:
    def __init__(self, directory):
        self.directory = directory
        self.cur_dir = os.getcwd()

    def __enter__(self):
        os.chdir(self.directory)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.cur_dir)


with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())