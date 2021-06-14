import datetime
import matplotlib.pyplot as plt

from string_parser import get_result, eval_


class GraphicMixin:

    def create(self, x, y):
        x_line = [datetime.datetime.now() - datetime.timedelta(days=x), datetime.datetime.now()]
        y_line = [get_result(y), datetime.datetime.now() - datetime.timedelta(days=int(eval_(y)))]
        plt.figure(1)
        plt.title('График функции |y| = {}'.format(y))
        plt.ylabel('Ось y')
        plt.xlabel('Ось x')
        plt.grid()
        plt.plot(x_line, y_line)
        plt.show()

