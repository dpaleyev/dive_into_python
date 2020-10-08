import os
import tempfile


class File:
    c = 0

    def __init__(self, path_name):
        self.path_name = path_name
        try:
            f = open(path_name, 'r')
        except FileNotFoundError:
            f = open(path_name, 'w')
        f.close()

    def __str__(self):
        return self.path_name

    def read(self):
        f = open(self.path_name, 'r')
        s = f.read()
        f.close()
        return s

    def write(self, s):
        f = open(self.path_name, 'w')
        f.write(s)
        f.close()
        return len(s)

    def __add__(self, obj):
        f1 = open(self.path_name, 'r')
        f2 = open(obj.path_name, 'r')
        new_path = os.path.join(tempfile.gettempdir(), 'file' + str(File.c) + '.txt')
        File.c += 1
        f = File(new_path)
        f.write(f1.read() + f2.read())
        f1.close()
        f2.close()
        return f

    def __iter__(self):
        self.f = open(self.path_name, 'r')
        return self

    def __next__(self):
        s = self.f.readline()
        if len(s) == 0:
            self.f.close()
            raise StopIteration
        return s
