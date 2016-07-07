from . import utilities as util


class DirDataFeeder(object):
    def __init__(self, dir):
        self.file_list = util.get_file_list(dir)
        self.counter = 0

    def get_batch(self, size, shuffle=False):
        result = []
        while len(result) < size:
            if shuffle:
                index = util.randint(0, len(self.file_list)-1)
            else:
                index = self.counter
                self.counter += 1

            result.append(self.file_list[index])
        return result
