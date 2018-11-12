#!/usr/bin/env python
import argparse
import os
import sys
import warnings

from django.core.management import execute_from_command_line

os.environ['DJANGO_SETTINGS_MODULE'] = 'healtheintent_api.tests.settings'


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--deprecation',
        choices=['all', 'pending', 'imminent', 'none'],
        default='imminent'
    )
    return parser


def parse_args(args=None):
    return make_parser().parse_known_args(args)


def runtests():
    parsed_args, unparsed_args = parse_args()

    only_this_app = r'^healtheintent_api(\.|$)'
    if parsed_args.deprecation == 'all':
        # Show all deprecation warnings from all packages
        warnings.simplefilter('default', category=DeprecationWarning)
        warnings.simplefilter('default', category=PendingDeprecationWarning)
    elif parsed_args.deprecation == 'pending':
        # Show all deprecation warnings
        warnings.filterwarnings('default', category=DeprecationWarning, module=only_this_app)
        warnings.filterwarnings('default', category=PendingDeprecationWarning, module=only_this_app)
    elif parsed_args.deprecation == 'imminent':
        # Show only imminent deprecation warnings
        warnings.filterwarnings('default', category=DeprecationWarning, module=only_this_app)
    elif parsed_args.deprecation == 'none':
        # Deprecation warnings are ignored
        pass

    argv = [sys.argv[0], 'test'] + unparsed_args
    return execute_from_command_line(argv)

if __name__ == '__main__':
    sys.exit(runtests())
