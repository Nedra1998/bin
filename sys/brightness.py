#!/usr/bin/python3

import sys
import util


def get_data():
    file_max = open("/sys/class/backlight/intel_backlight/max_brightness", "r")
    max_bright = file_max.readline()
    file_max.close()
    file_current = open("/sys/class/backlight/intel_backlight/brightness", "r")
    current_bright = file_current.readline()
    file_current.close()
    percent = float(current_bright) / float(max_bright) * 100
    return percent


def get_icon():
    pass


def main():
    percent = get_data()
    util.fmt_print({
        "{percent}": util.fmt_percent(percent),
        "{bar}": util.get_bar(percent)
    }, sys.argv[1])


if __name__ == "__main__":
    main()
