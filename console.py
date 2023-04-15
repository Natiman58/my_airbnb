#!/usr/bin/python3
"""
    A module for the console
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
        A class representing the console
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        return True
    def do_quit(self, arg):
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()