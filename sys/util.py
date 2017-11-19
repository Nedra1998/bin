import re


def get_bar(percent, minmum=False):
    if minmum is False:
        if percent <= 11.11:
            return ' '
        elif percent <= 22.22:
            return '\u2581'
        elif percent <= 33.33:
            return '\u2582'
        elif percent <= 44.44:
            return '\u2583'
        elif percent <= 55.55:
            return '\u2584'
        elif percent <= 66.66:
            return '\u2585'
        elif percent <= 77.77:
            return '\u2586'
        elif percent <= 88.88:
            return '\u2587'
        else:
            return '\u2588'
    elif minmum is True:
        if percent <= 12.5:
            return '\u2581'
        elif percent <= 25:
            return '\u2582'
        elif percent <= 37.5:
            return '\u2583'
        elif percent <= 50:
            return '\u2584'
        elif percent <= 62.5:
            return '\u2585'
        elif percent <= 75:
            return '\u2586'
        elif percent <= 87.5:
            return '\u2587'
        else:
            return '\u2588'


def fmt_print(data, fmt, end=''):
    for key, value in data.items():
        if type(value) is not str:
            data[key] = str(value)
    regex = re.compile("(" + '|'.join(data.keys()) + ")")
    fmt = regex.sub(lambda x: data[x.group()], fmt)
    print(fmt, end=end)


def fmt_percent(percent, whole=False):
    if whole is True:
        return "{:.0f}".format(percent)
    if percent >= 100:
        return "{:3.0f}".format(percent)
    elif percent >= 10:
        return "{:4.1f}".format(percent)
    else:
        return "{:4.2f}".format(percent)
