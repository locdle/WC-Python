#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'locle'

import unittest
import subprocess
import re


class TestWC(unittest.TestCase):
    def test_count_bytes_in_one_file(self):
        system_result = subprocess.getoutput("wc -c test.txt").lstrip()
        output = subprocess.getoutput("python3 wc.py -c test.txt")
        self.assertEqual(output, system_result)

    def test_another_count_bytes_in_one_file(self):
        system_result = subprocess.getoutput("wc -c test1.txt").lstrip()
        output = subprocess.getoutput("python3 wc.py -c test1.txt")
        self.assertEqual(output, system_result)

    def test_count_bytes_in_two_files(self):
        system_result = re.sub('  +', '', subprocess.getoutput("wc -c test.txt test1.txt"))
        output = subprocess.getoutput("python3 wc.py -c test.txt test1.txt")
        self.assertEqual(output, system_result)

    def test_count_lines_in_one_file(self):
        system_result = subprocess.getoutput("wc -l test.txt").lstrip()
        output = subprocess.getoutput("python3 wc.py -l test.txt")
        self.assertEqual(output, system_result)

    def test_another_count_lines_in_one_file(self):
        system_result = subprocess.getoutput("wc -l test1.txt").lstrip()
        output = subprocess.getoutput("python3 wc.py -l test1.txt")
        self.assertEqual(output, system_result)

    def test_count_lines_in_two_files(self):
        system_result = re.sub('  +', '', subprocess.getoutput("wc -l test.txt test1.txt"))
        output = subprocess.getoutput("python3 wc.py -l test.txt test1.txt")
        self.assertEqual(output, system_result)

    def test_count_character_in_one_file(self):
        system_result = subprocess.getoutput("wc -m test.txt").lstrip()
        output = subprocess.getoutput("python3 wc.py -m test.txt")
        self.assertEqual(output, system_result)

    def test_another_count_character_in_one_file(self):
        system_result = subprocess.getoutput("wc -m test1.txt").lstrip()
        output = subprocess.getoutput("python3 wc.py -m test1.txt")
        self.assertEqual(output, system_result)

    def test_count_character_in_two_file(self):
        system_result = re.sub('  +', '', subprocess.getoutput("wc -m test.txt test1.txt"))
        output = subprocess.getoutput("python3 wc.py -m test.txt test1.txt")
        self.assertEqual(output, system_result)

    def test_count_words_in_one_file(self):
        system_result = subprocess.getoutput("wc -w test.txt").lstrip()
        output = subprocess.getoutput("python3 wc.py -w test.txt")
        self.assertEqual(output, system_result)

    def test_another_count_words_in_one_file(self):
        system_result = subprocess.getoutput("wc -w test.txt").lstrip()
        output = subprocess.getoutput("python3 wc.py -w test.txt")
        self.assertEqual(output, system_result)

    def test_count_words_in_two_file(self):
        system_result = re.sub('  +', '', subprocess.getoutput("wc -w test.txt test1.txt"))
        output = subprocess.getoutput("python3 wc.py -w test.txt test1.txt")
        self.assertEqual(output, system_result)

if __name__ == '__main__':
    unittest.main()