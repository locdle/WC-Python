#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

__author__ = 'locle'

# check file exist and handle IO exception
def open_file(filename):
    try:
        fin = open(filename, 'r')
    except IOError:
        print("File %s not found" % filename)
        raise SystemExit


# count number of bytes in a file
def count_bytes(filename):
    open_file(filename)
    getsize = os.path.getsize(filename)
    return getsize


# count number of lines in a file
def count_lines(filename):
    open_file(filename)
    number_of_lines = len(open(filename).readlines())
    return number_of_lines


# count number of character in a file
def count_character(filename):
    open_file(filename)
    number_of_character = len(open(filename).read())
    return number_of_character


# count number of words in a file
def count_words(filename):
    open_file(filename)
    number_of_words = len(open(filename).read().split(None))
    return number_of_words


def main():
    # local count number of total if users input multiple file
    count_byte = 0
    count_line = 0
    count_char = 0
    count_word = 0

    # flag option
    byte = False
    line = False
    char = False
    word = False
    option = True

    if len(sys.argv) >= 2:
        if sys.argv[1] == "-h":
            print("The wc utility displays the number of lines, words, and bytes contained "
                  "in each input file, or standard input.\n"
                  "The following options are available:\n"
                  "\t-c\t      The number of bytes in each input file is written to the standard"
                  "output.  This will cancel out any prior usage of the -m option.\n"
                  "\t-l\t      The number of lines in each input file is written to the standard output.\n"
                  "\t-m\t      The number of characters in each input file is written to the standard output.\n"
                  "\t-w\t      The number of words in each input file is written to the standard output.\n"
                  "When an option is specified, wc only reports the information requested by"
                  "that option.\nThe order of output always takes the form of line, word,"
                  "byte, and file name.\nThe default action is equivalent to specifying the"
                  "-c, -l and -w options.")
        elif sys.argv[1] == "-c":
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
        elif sys.argv[1] == "-w":
            word = True
            for filename in sys.argv[2:]:
                print("%d %s" % (count_words(filename), filename))
                count_word += count_words(filename)
        else:
            option = False
            for filename in sys.argv[1:]:
                count_line += count_lines(filename)
                count_char += count_character(filename)
                count_word += count_words(filename)
                print("%d %d %d %s" % (count_lines(filename), count_words(filename), count_character(filename), filename))
            if len(sys.argv) > 2:
                print("%d %d %d %s" % (count_line, count_word, count_char, "total"))

        if len(sys.argv) > 3 and option:
            if byte:
                print("%d total" % count_byte)
            elif line:
                print("%d total" % count_line)
            elif char:
                print("%d total" % count_char)
            elif word:
                print("%d total" % count_word)
    else:
        print("usage wc textfile1 [textfile2 ...]")


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        sys.exit(1)
    else:
        sys.exit(0)