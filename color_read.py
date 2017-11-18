#!/usr/lib/python3


def set_color(red, green, blue):
    print("\033[48;2;{};{};{}m".format(red, green, blue), end='')


def reset():
    print("\033[49m", end='')


def main():
    while True:
        hex_color = input("Enter Hex:").lstrip('#')
        if hex_color == "quit":
            break
        rgb_color = tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
        rgb5_color = tuple(x / 51.0 for x in rgb_color)
        xterm_color = (
            (36 * int(round(rgb5_color[0]))) +
            (6 * int(round(rgb5_color[1]))) + int(round(rgb5_color[2]))) + 16
        print("  COLOR:   ", end='')
        set_color(rgb_color[0], rgb_color[1], rgb_color[2])
        print("       ", end='')
        reset()
        print()
        print("  HEX:     #{}".format(hex_color.upper()))
        print("  RGB:     {}".format(rgb_color))
        print("  RGB 5:   {}".format(rgb5_color))
        print("  XTERM:   {}".format(xterm_color))


if __name__ == "__main__":
    main()
