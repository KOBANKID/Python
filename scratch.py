#!/usr/bin/env python3
"""
This module is for creating .gitkeep in empty directories.
"""
import subprocess
import argparse
import os
import sys

def mylist(args):
    """
    mylist
    """
    print('mylist function is called')
    print(vars(args))
    str_list_args = "This is %(dir)s" %vars(args)
    print(str_list_args)

def keep(args):
    """
    keep
    """
    print('keep function is calle')
    command = "find %(dir)s -type d -name .git -prune -o -type d -empty -exec touch {}/%(keeper)s \;" % vars(args)
    # command = "find %(dir)s -type d -name .git -prune -o -type d -empty;" % vars(args)
    result = subprocess.run(command, shell=True, check=True)
    print(result)
    print("result.returncode={0}".format(result.returncode))

    if result.returncode > 0:
        print("keeper error")
        sys.exit(1)

def main():
    """
    main
    """
    my_parser = argparse.ArgumentParser(description="git keeper")

    # dir option
    my_parser.add_argument('-d', '--dir', type=str, help='specify the directory for analysis',\
                           default=os.getcwd())
    my_parser.set_defaults(handler=mylist)

    # keeper option
    my_parser.add_argument('--keeper', type=str, \
                           help='file name for gitkeep. default is ".gitkeep"', default='.gitkeep')
    my_parser.set_defaults(handler=keep)

    # parse arguments
    args = my_parser.parse_args()
    print('dir={0}, keeper={1}'.format(args.dir, args.keeper))

    args.handler(args)

if __name__ == "__main__":
    main()
