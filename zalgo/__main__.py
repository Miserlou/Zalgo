#! /usr/bin/env python
from __future__ import print_function

import argparse
import sys
import xerox
from . import zalgo


def convert_zalgo(text, intensity=50, copy=False):
    input_text = u' '.join(text)
    zalgotext = zalgo.zalgo(input_text, intensity)

    if copy:
       xerox.copy(u'' + zalgotext)

    return zalgotext


def get_parser():
    parser = argparse.ArgumentParser(description='Command line zalgo.')
    parser.add_argument('text', metavar='TEXT', type=str, nargs='*',
                        help='the text to zalgo')
    parser.add_argument('-c','--copy', help='copy result to the clipboard.',
                        default=False, dest='copy', action='store_true')
    parser.add_argument('-i','--intensity',
                        help='Intensity of zalgo. 1-200. Default 50.',
                        choices=range(1, 201), default=50, type=int)

    return parser


def command_line_runner():
    parser = get_parser()
    args = parser.parse_args()
    if not args.text:
        parser.print_help()
        return
    else:
        zalgotext = convert_zalgo(args.text, args.intensity, args.copy)

        if not args.copy:
            print(zalgotext)



if __name__ == '__main__':
    command_line_runner()
