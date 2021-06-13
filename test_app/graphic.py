import datetime

import matplotlib.pyplot as plt


class GraphicMixin:

    @staticmethod
    def _multiply(_x_array, _days):
        return [_date_obj+datetime.timedelta(datetime.datetime.now().day*_days) for _date_obj in _x_array]

    @staticmethod
    def _split(_x_array, _days):
        return [_date_obj-datetime.timedelta(datetime.datetime.now().day*_days) for _date_obj in _x_array]

    @staticmethod
    def _square(_x_array, _days):
        return [_date_obj+datetime.timedelta(datetime.datetime.now().day**_days) for _date_obj in _x_array]

    def create(self, x, y):
        # x = [datetime.datetime.now() - datetime.timedelta(days=8), datetime.datetime.now()]
        y_line = self._multiply(x, 5)  # TODO logic
        plt.figure(1)
        plt.title('График функции |y| = {}'.format(y))
        plt.ylabel('Ось y')
        plt.xlabel('Ось x')
        plt.grid()
        plt.plot(x, y_line)
        plt.show()


GraphicMixin().create(
    [datetime.datetime.now() - datetime.timedelta(days=8), datetime.datetime.now()],
    't*5'
)