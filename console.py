#!/usr/bin/python3
import sys
import cmd
# from models.base_model import BaseModel
# from models.engine.file_storage import FileStorage
"""consol module for AitBnB front end project"""


class HBNBCommand(cmd.Cmd):
    """
    attributes: prompt, file

    methods: EOF, quite
    """
    prompt = "(hbnb) "
    file = None

    def do_EOF(self, args):
        """ Handles end of file"""
        print()
        return True

    def do_quit(self, args):
        """Exit the console"""
        sys.exit()

    def do_create(self, args):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
