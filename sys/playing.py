#!/usr/bin/python3

import sys
import util
import subprocess
import json
from pprint import pprint
from csv import reader


def get_dict():
    metadata = subprocess.run(
            ["playerctl", "metadata"],
            stdout=subprocess.PIPE).stdout.decode('utf-8')
    import ast
    metadata = metadata.strip('{')
    metadata = metadata.strip('}')
    in_quote = False
    meta_list = list()
    string = str()
    for char in metadata:
        if char == '\"' or char == '\'':
            if in_quote is False:
                in_quote = True
            else:
                in_quote = False
        if char == ',' and in_quote is False:
            meta_list.append(string)
            string = str()
        else:
            string += char
    metadata = meta_list
    data = dict()
    for item in metadata:
        item = item.split(': ')
        item[1] = item[1].strip('<')
        item[1] = item[1].strip('>')
        item[0] = item[0].strip('\"')
        item[0] = item[0].strip('\'')
        item[0] = item[0].split(':')[1]
        item[1] = item[1].strip('\"')
        item[1] = item[1].strip('\'')
        if item[1].startswith("uint64 "):
            item[1] = item[1][7:]
        if item[1][0] == '[' and item[1][-1] == ']':
            item[1] = item[1][1:-1]
            item[1] = item[1].split(', ')
            for i, it in enumerate(item[1]):
                item[1][i] = it.strip('\"')
                item[1][i] = it.strip('\'')
            item[1] = ", ".join(item[1])

        if type(item[1]) is str:
            try:
                item[1] = "{:d}".format(int(item[1]))
            except ValueError:
                pass
        if type(item[1]) is str:
            try:
                item[1] = "{:.2f}".format(float(item[1]))
            except ValueError:
                pass

        data[item[0].lower()] = item[1]
    return data
#  print(metadata)


def get_data():
    status = subprocess.run(
            ["playerctl", "status"], stdout=subprocess.PIPE,
            stderr=subprocess.PIPE).stdout.decode('utf-8')
    if status.strip() == "Playing":
        status = True
    elif status.strip() == "Paused":
        status = False
    else:
        status = -1
    return status


def get_play_pause(status):
    if status == False:
        return '\uf04b'
    elif status == True:
        return '\uf04c'
    else:
        return ''


def main():
    status = get_data()
    data = dict()
    if status != -1:
        data = get_dict()
    data['status'] = str(status)
    data['play_pause'] = get_play_pause(status)
    data['next'] = '\uf051'
    data['prev'] = '\uf048'
    data['icon'] = '\uf001'
    if len(sys.argv) == 2:
        util.fmt_print(data, sys.argv[1])
    if status is True and len(sys.argv) >= 3:
        util.fmt_print(data, sys.argv[1])
    elif status is False and len(sys.argv) >= 3:
        util.fmt_print(data, sys.argv[2])
    elif len(sys.argv) >= 4:
        util.fmt_print(data, sys.argv[3])


if __name__ == "__main__":
    main()
