#!/usr/bin/python3

import util
import subprocess
import sys
import platform


def get_count_deb():
    count = 0
    packages = list()
    result = subprocess.run(
            ["apt-get", "--just-print", "upgrade"],
            stdout=subprocess.PIPE).stdout.decode('utf-8').split('\n')
    counting = False
    for line in result:
        if line == "The following packages will be upgraded:":
            counting = True
        elif line.endswith("not upgraded."):
            counting = False
        elif counting is True:
            count += len(line.split())
            packages += line.split()
    return count, packages


def get_count_arch():
    count = [0, 0]
    print(count)
    result = subprocess.run(
            ["checkupdates"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    count[0] = result.count("\n")
    try:
        result = subprocess.run(
                ["cower", "-u"], stdout=subprocess.PIPE).stdout.decode('utf-8')
    except subprocess.CalledProcessError as cp_error:
        result = cp_error.output
    except:
        result = "?"
    count[1] = result.count('\n')
    return count


def get_data(dist):
    if dist == 'Ubuntu':
        return get_count_deb()
    elif dist == 'Arch':
        return get_count_arch()
    else:
        return (0,0)


def get_distro():
    return platform.dist()[0].title();


def pkg_manager(dist):
    if dist == 'Ubuntu':
        return "apt"
    elif dist == "Arch":
        return ["pacman", "AUR"]
    elif dist == "Debian":
        return "apt-get"
    else:
        return "(NULL)"


def get_distro_icon(dist):
    if dist == 'Ubuntu':
        return '\uf31b'
    elif dist == "Arch":
        return '\uf300'
    elif dist == "Debian":
        return '\uf302'
    else:
        return '\ue712'

def list_pkg():
    dist = get_distro()
    title = get_distro_icon(dist) + ' ' + dist + ' (' + pkg_manager(dist) + ')'
    count, pkg = get_data(dist)
    print(title + '\n \u2022 ' + '\n \u2022 '.join(pkg))
    #  subprocess.run(["notify-send", title, "\"None\""])

def notify_pkg():
    dist = get_distro()
    title = get_distro_icon(dist) + ' ' + dist + ' (' + pkg_manager(dist) + ')'
    count, pkg = get_data(dist)
    content = '\n \u2022 ' + '\n \u2022 '.join(pkg)
    subprocess.run(["notify-send", title, content])


def main():
    if sys.argv[1] == "--list":
        list_pkg()
        exit()
    elif sys.argv[1] == "--notify":
        notify_pkg()
        exit()
    dist = get_distro()
    count, pkg = get_data(dist)
    data = dict()
    data['icon'] = get_distro_icon(dist)
    if dist == "Ubuntu":
        data['apt'] = count
        data['total'] = count
    elif dist == "Arch":
        data['total'] = count[0] + count[1]
        data['pacman'] = count[0]
        data['aur'] = count[1]
    util.fmt_print(data, sys.argv[1])


if __name__ == "__main__":
    main()
