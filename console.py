#!/usr/bin/python3
"""A Module that defines the HBnB console"""

import cmd
import json
import sys
import re
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A class the defines the  HBNBCommand for CLI """

    prompt = '(hbnb) '
    my_class = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def do_EOF(self):
        """EOF comamand to exit the program """
        return True

    def emptyline(self):
        """Does nothing when empty line is given """
        pass

    def do_help(self, line):
        """To get help on a command, type help <topic>"""
        return super().do_help(line)

    def do_create(self, line):
        """Creates a new instance of BaseModel saves it and prints the id"""
        arguments = line.split()
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.my_class.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.my_class[arguments[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        basesd on the class name and id
        """
        arguments = line.split()
        if not line:
            print("** class name missing **")
            return
        elif arguments[0] not in HBNBCommand.my_class.keys():
            print("** class doesn't exist **")
            return
        elif len(arguments) < 2:
            print("** instance id missing **")
            return
        obj = storage.all()
        key = "{}.{}".format(arguments[0], arguments[1])
        my_instance = obj.get(key, None)
        if my_instance is None:
            print("** no instance found **")
            return
        print(my_instance)

    def do_destroy(self, line):
        """Deletes a class instance based  on the class name and id"""
        arguments = line.split()
        if not line:
            print("** class name missing **")
            return
        elif arguments[0] not in HBNBCommand.my_class.keys():
            print("** class doesn't exist **")
            return
        elif len(arguments) < 2:
            print("** instance id missing **")
            return
        temp_obj = storage.all()
        key = "{}.{}".format(arguments[0], arguments[1])
        my_instance = temp_obj.get(key, None)
        if my_instance is None:
            print("** no instance found **")
            return
        del temp_obj[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        arguments = line.split()
        all_objs = storage.all()

        if len(arguments) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if arguments[0] not in HBNBCommand.my_class.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for k, v in all_objs.items()
                  if type(v).__name__ == arguments[0]])
            return

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        """
        arguments = line.split()
        if not line:
            print("** class name missing **")
            return
        if arguments[0] not in HBNBCommand.my_class:
            print("** class doesn't exist **")
            return
        elif len(arguments) < 2:
            print("** instance id missing **")
            return
        my_obj = storage.all()
        key = "{}.{}".format(arguments[0], arguments[1])
        my_instance = my_obj.get(key, None)
        if my_instance is None:
            print("** no instance found **")
            return
        match_json = re.findall(r"{.*}", line)
        if match_json:
            payload = None
            try:
                payload: dict = json.loads(match_json[0])
            except Exception:
                print("** invalid syntax")
                return
            for k, v in payload.items():
                setattr(my_instance, k, v)
            storage.save()
            return
        if len(arguments) < 3:
            print("** attribute name missing **")
            return
        if len(arguments) < 4:
            print("** value missing **")
            return
        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", arguments[3])
        if first_attr:
            setattr(my_instance, arguments[2], first_attr[0])
        else:
            val = arguments[3].split()
            setattr(my_instance, arguments[2], parse_str(val[0]))
        storage.save()

    def parse_str(arg):
        """Converts the input argument to an integer, float,
        or leaves it as a string
        """
        parsed = re.sub("\"", "", arg)
        if is_int(parsed):
            return int(parsed)
        elif is_float(parsed):
            return float(parsed)
        else:
            return arg

    def is_int(n):
        """Determines whether the input is an integer or not"""
        try:
            num1 = float(n)
            num2 = int(num1)
        except (TypeError, ValueError):
            return False
        else:
            return num1 == num2

    def is_float(n):
        """Determines whether the input is float or not"""
        try:
            num = float(n)
        except (TypeError, ValueError):
            return False
        else:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
