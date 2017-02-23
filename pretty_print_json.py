#!/usr/bin/env python
# coding=utf-8

"""
example code of reading from stdin.

This program decode json and pretty print it.
"""

from __future__ import print_function, unicode_literals

import sys
import json


def main():
    try:
        o = json.load(sys.stdin)
        json.dump(o, sys.stdout, indent=4)
        print()
    except ValueError as e:
        print("JSON decode failed: %s" % ("".join(e.args),))
        sys.exit(1)


if __name__ == '__main__':
    main()
