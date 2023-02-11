#!/usr/bin/python3
import sys
import cmd
import shlex
import models
import re
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
"""consol module for AitBnB front end project"""


class HBNBCommand(cmd.Cmd):
    """
    attributes: prompt, file

    methods: EOF, quite
    """
    prompt = "(hbnb) "
    classes = [
                'BaseModel',
                'Amenity',
                'State',
                'Place',
                'Review',
                'User',
                'City'
                ]
    file = None

    def do_EOF(self, args):
        """ Handles end of file"""
        print()
        return True

    def do_quit(self, args):
        """Exit the console"""
        sys.exit()

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
