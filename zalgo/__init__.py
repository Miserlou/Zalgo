#! /usr/bin/env python

# I hate Python 3.
from __future__ import print_function

import argparse
import sys
import xerox
from zalgo import zalgo

def convert_zalgo(text, intensity=50, copy=False):

    input_text = u' '.join(text)

    to_print = zalgo(input_text, intensity)
    to_print = to_print.decode('utf8')

    if copy:
       xerox.copy(u'' + to_print)

    print(to_print)

    return

def get_parser():

    parser = argparse.ArgumentParser(description='Command line zalgo.')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
            help='the text to zalgo')
    parser.add_argument('-c','--copy', help='copy result to the clipboard.', default=False, dest='copy', action='store_true')
    parser.add_argument('-f','--file', help='list all of the available emoji.', default=False, dest='list', action='store_true')
    parser.add_argument('-i','--intensity', help='Intensity of zalgo. 1-200. Default 50.', choices=xrange(1, 201), default=50, type=int)
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)

    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if not args['query'] and not args['list'] and not args['all']:
        parser.print_help()
        return

    if args['query']:
        convert_zalgo(args['query'], args['intensity'], args['copy'])

if __name__ == '__main__':
    command_line_runner()
