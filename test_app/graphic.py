import datetime
import random
import string

import matplotlib.pyplot as plt

from .string_parser import get_result
from path_module import get_path


class GraphicMixin:

    @staticmethod
    def get_name(size=16, chars=string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def create(self, x, y):
        x_line = [datetime.datetime.now() - datetime.timedelta(days=x), datetime.datetime.now()]
        y_line = [get_result(y), datetime.datetime.now()]
        plt.figure(1)
        plt.title('График функции |y| = {}'.format(y))
        plt.ylabel('Ось y')
        plt.xlabel('Ось x')
        plt.grid()
        plt.plot(x_line, y_line)

        _name = self.get_name()
        _path = get_path()+"/media/{}".format(_name)
        plt.savefig(_path)
        return "/media/{}.png".format(_name)
