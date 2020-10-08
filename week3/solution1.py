import os.path


class FileReader:
    def __init__(self, link):
        self.link = link

    def read(self):
        try:
            f = open(self.link)
            return f.read()
        except FileNotFoundError:
            return ''
