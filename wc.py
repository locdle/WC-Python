#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

__author__ = 'locle'


def open_file(filename):
    try:
        fin = open(filename, 'r')
        text = fin.read()
        fin.close()
    except IOError:
        print("wc: %s: open: No such file or directory" % filename)
        raise SystemExit


def count_bytes(filename):
    open_file(filename)
    getsize = os.path.getsize(filename)
    return getsize


def main():
    count_byte = 0

    if len(sys.argv) >= 2:
        if sys.argv[1] == "-c":
            for filename in sys.argv[2:]:
                print("%d %s" % (count_bytes(filename), filename))
                count_byte += count_bytes(filename)
        if len(sys.argv) > 3:
            print("%d total" % count_byte)
    else:
        print("usage wc textfile1 [textfile2 ...]")


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        sys.exit(1)
    else:
        sys.exit(0)