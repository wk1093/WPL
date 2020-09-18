import run
import shell
import sys


def get_args(args):
    if len(args) > 2:
        print("Too Many Arguments")
        return
    elif len(args) < 2:
        shell.shell()
        return
    elif len(args) == 2:
        if args[1] in ("-h", "-help"):
            print("USAGE: wpl [FILE]")
            return
        else:
            run.run(sys.argv)


get_args(sys.argv)