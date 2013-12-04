#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Oblique strategies random displayer.

[wikipedia]: https://en.wikipedia.org/wiki/Oblique_Strategies
"""

import os
import sys
import argparse
import yaml
import random

APP_PATH = os.path.dirname(os.path.realpath(__file__))
STRATEGIES_FILE = os.path.join(APP_PATH, 'data', 'strategies.yml')

def _load(strategies_file):
    """Load a strategies file.

    strategies_file -- YAML file with a list of strategies.

    Returns all list of strategies.
    """
    if not os.path.exists(strategies_file):
        msg = "Can't find strategies file '{0}'".format(STRATEGIES_FILE)
        raise ValueError(msg)

    return yaml.load(open(strategies_file, 'rb'))

def get_random(strategies_file=STRATEGIES_FILE):
    """Get a random oblique strategy.

    strategies_file -- YAML file with a list of strategies.

    Return the oblique strategy
    """
    strategies = _load(strategies_file)

    return random.choice(strategies)

def main():
    """Main."""
    try:
        description = 'Randomly pick one oblique strategy.'
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument('-n', type=int, default=1,
                            help='Number of strategies to pick')

        args = parser.parse_args()

        for i in range(args.n):
            print(get_random())
    except ValueError, msg:
        return msg

if __name__ == '__main__':
    sys.exit(main())
