#!/usr/bin/env python3

# Zenstat is a small TUI to make netstat easier by offering preset commands 
# and output formatting. You select from a TUI list and the command is run
# in the terminal until you hit 'q', the you're sent back to the list, hit
# it again to quit the program.

import subprocess, sys, os

# Import terminal library to enable raw mode
import tty, termios

def ansi_move_line_up(n):
    print(f"\033[{n}A", end="")
    print("\033[1G", end="")

def ansi_move_line_down(n):
    print(f"\033[{n}B", end="")
    print("\033[1G", end="")

def ansi_clear_current_line():
    print("\033[K", end="")
    print("\033[1G", end="")

def ansi_clear_everything():
    print("\033[2J", end="")
    print("\033[1;1H", end="")


command_list 

def zenstat_menu():

    # Before clearing, save the state of the terminal buffer so we can restore
    # the characters later.


    selected = 0
    options = [
        "- Routing Table",
        "- Statistics",
        "- Show all listening ports with process names",
        "- Show all established connections with process names",
        "- Quit",
    ]

    for i in range(len(options)):
        ansi_clear_current_line()
        ansi_move_line_down(1)

    while True:
        # Navigate with hjkl keys, highlight seleted option by changing
        # background color.

        # Clear each line by moving backwards and clearing a line per
        # iteration

        for i in range(len(options)):
            ansi_clear_current_line()
            ansi_move_line_up(1)

        for i, option in enumerate(options):
            if i == selected:
                print("\033[7m", end="")
            print(option, end='')
            print("\033[0m", end="")
            ansi_move_line_down(1)
            # flush stdout
            sys.stdout.flush()


        # Get user input directly without stdin

        if sys.stdin.isatty():
            c = sys.stdin.read(1)

            match c:
                case "j":
                    selected = (selected + 1) % len(options)
                case "k":
                    selected = (selected - 1) % len(options)
                case "q":
                    break

def main():
    # Enable raw mode
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())

    zenstat_menu()


    # Disable raw mode
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


if __name__ == '__main__':
    main()
