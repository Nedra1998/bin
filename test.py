#!/usr/bin/python3

import subprocess

print("ENTERING VIM")
p = subprocess.run(["vim"], shell=True, stdin=subprocess.PIPE)
print("EXIT VIM")
input("HELLO!")
