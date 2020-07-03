#!/usr/bin/env python3
"""
My Module
"""
import subprocess
import argparse
import os
# import sys

def invoke_command(commands: str) -> int:
    """
    invoke_command
    """
    print(commands)
    subprocess.run(commands, shell=True, check=True)

    return 0

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
    # command = "find %(dir)s -type d -name .git -prune -o -type d -empty -exec touch {}/%(keeper)s \;" % vars(args)
    command = "find %(dir)s -type d -name .git -prune -o -type d -empty;" % vars(args)
    subprocess.run(command, shell=True, check=True)
    # print(result[1])
    # if result[0] > 0:
    #     sys.exit(1)

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
    my_parser.add_argument('--keepr', type=str, \
                           help='file name for gitkeep. default is ".gitkeep"', default='.gitkeep')
    my_parser.set_defaults(func=keep)

    args = my_parser.parse_args() # Analysis arguments
    print('arg1='+args.dir)

    args.handler(args)
    args.func(args)

if __name__ == "__main__":
    main()
