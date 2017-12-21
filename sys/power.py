#!/usr/bin/python3

import psutil
import util
import sys

def get_data():
    if not hasattr(psutil, "sensors_battery"):
        return sys.exit("platform not supported")
    battery = psutil.sensors_battery()
    precent = battery.percent
    minute, sec = divmod(battery.secsleft, 60)
    hour, minute = divmod(minute, 60)
    charging = False
    if hour < 0 or minute < 0 or sec < 0:
        hour *= -1
        minute *= -1
        sec *= -1
        charging = True
    time = [hour, minute, sec]
    return precent, charging, time


def get_icon(percent, charging):
    if charging is True:
        return '\uf1e6'
    elif percent <= 20:
        return '\uf244'
    elif percent <= 40:
        return '\uf243'
    elif percent <= 60:
        return '\uf242'
    elif percent <= 80:
        return '\uf241'
    else:
        return '\uf240'


def main():
    percent, charging, time = get_data()
    if sys.argv[1] == "--charging":
        if charging is True:
            print("Charging", end='')
        else:
            print("Discharging", end='')
        return
    data = {"percent": util.fmt_percent(percent),
            "bar": util.get_bar(percent),
            "icon": get_icon(percent, charging),
            "H": "{:02}".format(time[0]),
            "M": "{:02}".format(time[1]),
            "S": "{:02}".format(time[2])}
    util.fmt_print(data, sys.argv[1])


if __name__ == "__main__":
    main()
