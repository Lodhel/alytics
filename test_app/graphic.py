import datetime
import string

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

    def _parse_string(self, string_input):
        symbols_main = '^*/+-'
        symbols_main_validated = ['^', '*', '/', '+', '-']
        formula = [x for x in string_input if x in string.digits + symbols_main + 't']
        validation = {
            "t": None,
            't2': None,
            "operation": '',
            "num": 0,
            "sum": '',
            "result": []
        }

        for symbol in formula:
            if symbol == 't' and not validation['t']:
                validation['sum'] += '{}'.format(symbol)
                validation['t'] = True
            if symbol == 't' and validation['t']:
                validation['sum'] += '{}'.format(symbol)
                validation['t2'] = True
            if symbol in symbols_main_validated:
                validation['sum'] += '{}'.format(symbol)
                validation['operation'] = symbol
            if symbol in string.digits:
                validation['sum'] += '{}'.format(symbol)
                validation['num'] = symbol

            if validation['t'] and validation['operation'] and validation['num']:
                if validation['operation'] == '*':
                    validation['result'].append(self._multiply(
                        [datetime.datetime.now() - datetime.timedelta(days=8), datetime.datetime.now()],
                        int(validation['num'])
                    ))

            if validation['t'] and validation['operation'] and validation['t2']:
                if validation['operation'] == '*':
                    validation['result'].append(self._square(
                        [datetime.datetime.now() - datetime.timedelta(days=8), datetime.datetime.now()],
                        2
                    ))

            return validation['result']

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


test = [GraphicMixin()._parse_string('t*5')]
print(test)