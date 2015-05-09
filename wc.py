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


def count_lines(filename):
    open_file(filename)
    number_of_lines = len(open(filename).readlines())
    return number_of_lines


def count_character(filename):
    open_file(filename)
    number_of_character = len(open(filename).read())
    return number_of_character


def main():
    count_byte = 0
    count_line = 0
    count_char = 0

    byte = False
    line = False
    char = False

    if len(sys.argv) >= 2:
        if sys.argv[1] == "-c":
            byte = True
            for filename in sys.argv[2:]:
                print("%d %s" % (count_bytes(filename), filename))
                count_byte += count_bytes(filename)
        elif sys.argv[1] == "-l":
            line = True
            for filename in sys.argv[2:]:
                print("%d %s" % (count_lines(filename), filename))
                count_line += count_lines(filename)
        elif sys.argv[1] == "-m":
            char = True
            for filename in sys.argv[2:]:
                print("%d %s" % (count_character(filename), filename))
                count_char += count_character(filename)

        if len(sys.argv) > 3:
            if byte:
                print("%d total" % count_byte)
            elif line:
                print("%d total" % count_line)
            elif char:
                print("%d total" % count_char)
    else:
        print("usage wc textfile1 [textfile2 ...]")


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        sys.exit(1)
    else:
        sys.exit(0)