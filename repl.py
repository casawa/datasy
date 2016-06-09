"""
Provides a command line interface to datasy.
"""

from __future__ import print_function
import datasy
from datasy import *

#class REPL:

exit_commands = ['exit']

def process(raw_command):
    pass

def main():
    print('Welcome to the datasy command line')
    while True:
        raw_command = raw_input('>> ')
        if raw_command in exit_commands:
            break


if __name__ == '__main__':
    main()


