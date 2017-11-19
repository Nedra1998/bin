#!/usr/bin/python3

import util
import subprocess
import sys
import platform


def get_data(dist):
    if dist == 'Ubuntu':
        result = subprocess.run(
            ["apt", "list", "--upgradable"],
            stdout=subprocess.PIPE).stdout.decode('utf-8')
        return len(result.split('\n')[1:-1])
    elif dist == 'Arch':
        count = [0, 0]
        result = subprocess.run(
            ["checkupdates"], stdout=subprocess.PIPE).stdout.decode('utf-8')
        count[0] = result.count("\n")
        try:
            result = subprocess.run(
                ["cower", "-u"], stdout=subprocess.PIPE).stdout.decode('utf-8')
        except subprocess.CalledProcessError as cp_error:
            result = cp_error.output
        except:
            result = '?'
        count[1] = result.count('\n')
        return count


def get_distro():
    return platform.dist()[0]


def get_distro_icon(dist):
    if dist == 'Ubuntu':
        return '\uf30c'
    elif dist == "Arch":
        return '\uf300'
    elif dist == "Debian":
        return '\uf302'
    else:
        return '\ue712'


def main():
    print("hello")
    dist = get_distro()
    count = get_data(dist)
    data = dict()
    data['{icon}'] = get_distro_icon(dist)
    if dist == "Ubuntu":
        data['{apt}'] = count
        data['{total}'] = count
    elif dist == "Arch":
        data['{total}'] = count[0] + count[1]
        data['{pacman}'] = count[0]
        data['{aur}'] = count[1]
    util.fmt_print(data, sys.argv[1])


if __name__ == "__main__":
    main()
