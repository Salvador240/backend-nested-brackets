#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Salvador240 with help from instructor"

import sys
opening_brackets = ['{', '[', '(', '(*', '<']
closing_brackets = ['}', ']', ')', '*)', '>']


def is_valid(line):
    stack = []
    index = 0
    while line:
        tok = line[0]
        # handle corner cases for the '(*' and the '*)'
        # inspect first two chars of line to see if they match for eyebrow tokens
        if line[:2] == opening_brackets[3] or line[:2] == closing_brackets[3]:
            tok = line[:2]

        index += 1
        if tok in opening_brackets:
            stack.append(tok)
        if tok in closing_brackets:
            # check if closing token matches opening token on top of stack.
            # if they are not pairs, then nesting is not valid
            i = closing_brackets.index(tok)
            expected_opener = opening_brackets[i]
            if expected_opener != stack.pop():
                return ("No", index)

        line = line[len(tok):]
    if len(stack) == 0:
        return ("Yes")
    else:
        return ("No", index)


def main(args):
    """Add your code here"""

    with open('input.txt') as f:
        with open('output.txt', 'w') as output_file:
            for line in f:
                # print("checking line {}".format(line))
                result_line = is_valid(line)
                print(result_line)
                output_file.write(str(result_line) + '\n')


if __name__ == '__main__':
    main(sys.argv)
