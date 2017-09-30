#!/usr/bin/python3

import random

project_school = ["Discrete", "Differential", "Graphics", "Physics"]
project_programming = [
    "Forma", "Aequus", "CLI", "Temporis", "Quickstart", "laboris"
]


def main():
    print(random.choice(project_school))
    print(random.choice(project_programming))


if __name__ == "__main__":
    main()
