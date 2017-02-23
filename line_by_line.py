#!/usr/bin/env python
# coding=utf-8

"""example code of reading from stdin.

This program show input text in upper case.

"""

from __future__ import print_function, unicode_literals

import sys


def process_line(line):
    print(line.upper(), end="")


def main():
    line = sys.stdin.readline()

    while line:
        process_line(line)
        line = sys.stdin.readline()


if __name__ == '__main__':
    main()
