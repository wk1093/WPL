import sys, WPL, os

def get_args(args):
    if len(args) > 2:
        print("Too Many Arguments")
        return
    elif len(args) < 2:
        print("Not Enough Aruments")
        return
    elif len(args) == 2:
        if args[1] in ("-h", "-help"):
            print("USAGE: wpl [FILE]")
            return
        else:
            return args[1]

def run(args):
    argument = get_args(args)
    if os.path.isfile(argument):
        WPL.run('<stdin>', '', argument)
    else:
        print("File Does Not Exist")