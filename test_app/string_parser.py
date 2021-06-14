import datetime

OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}

MONTHS = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}


def eval_(formula):
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s == 't':
                number += str(datetime.datetime.now().day)
            if s in '1234567890.':
                number += s
            elif number:
                yield float(number)
                number = ''
            if s in OPERATORS or s in "()":
                yield s
        if number:
            yield float(number)

    def shunting_yard(parsed_formula):
        stack = []
        for token in parsed_formula:
            if token in OPERATORS:
                while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                stack.append(token)
            else:
                yield token
        while stack:
            yield stack.pop()

    def calc(polish):
        stack = []
        for token in polish:
            if token in OPERATORS:
                y, x = stack.pop(), stack.pop()
                stack.append(OPERATORS[token][1](x, y))
            else:
                stack.append(token)
        return stack[0]

    return calc(shunting_yard(parse(formula)))


def get_result(formula):
    day = int(eval_(formula))
    month = int(datetime.datetime.now().month)
    month_days = MONTHS[month]
    year = int(datetime.datetime.now().year)

    if day <= 0:
        while day <= 0:
            if day == 0:
                month -= 1
                if month == 0:
                    month = 1
                    year -= 1
            day += month_days
            month -= 1
            if month == 0:
                month = 1
                year -= 1

    if day > month_days:
        while day > month_days:
            day -= month_days
            month += 1
            if month == 13:
                month = 1
                year += 1

    return datetime.datetime(day=day, year=year, month=month)
