#!/usr/bin/python3
"""
    A module for the console
"""

import cmd
from models.base_model import BaseModel
from sys import argv
from models import storage


class HBNBCommand(cmd.Cmd):
    """
        A class representing the console
    """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """ EOF command interpreter """
        return True

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_create(self, arg):
        """
        Create a new instance of the BaseModel class
        and saves it to a json file and prints the id
        """
        if not arg:
            print("** class name missing ** ")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
            prints the string representation of an instance based on
            the class name and id
        """
        classes = {
            'BaseModel': BaseModel
        }
        args = arg.split()
        if len(args) == 0:
            print("** class name missing ** ")
        elif len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """
            deletes an instance based on calss name and id
        """
        classes = {
            'BaseModel': BaseModel
        }
        args = arg.split()
        if len(args) == 0:
            print(" ** class name missing ** ")
        elif len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            key = args[0] + '.' + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]

    def do_all(self, arg):
        """
            prints all instances based on class name or
            'all' command
        """
        obj_array = []
        all_objs = storage.all()

        if arg == '':
            for key in all_objs.keys():
                obj = all_objs[key]
                obj_array.append(str(obj))
            print(obj_array)
        else:
            try:
                class_obj = eval(arg)
                for key in all_objs.keys():
                    obj = all_objs[key]
                    if type(obj) == class_obj:
                        obj_array.append(str(obj))
                print(obj_array)
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
