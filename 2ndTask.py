import csv


class ReadItems:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.open = open(self.file, self.mode)
        return self.open

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.open.close()


def show_items(file):
    with ReadItems(file, 'r') as items:
        data = csv.DictReader(items, delimiter=',')
        for item in data:
            print(item)


show_items('items.csv')