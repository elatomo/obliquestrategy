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

# cached files
_cache = {}

def _load(strategies_file, skip_cache):
    """Load a strategies file.

    strategies_file -- YAML file with a list of strategies.
    skip_cache -- Whether to skip any cached file contents or reload the whole file.

    Returns a list of all strategies contained in the file.
    """
    global _cache
    strategies = _cache.get(strategies_file)

    if not skip_cache and strategies:
        return strategies
    else:
        if not os.path.exists(strategies_file):
            msg = "Can't find strategies file '{0}'".format(STRATEGIES_FILE)
            raise ValueError(msg)
        strategies = yaml.load(open(strategies_file, 'rb'))
        _cache[strategies_file] = strategies
        return strategies

def get_random(strategies_file=STRATEGIES_FILE, skip_cache=False):
    """Get a random oblique strategy.

    strategies_file -- YAML file with a list of strategies.
    skip_cache -- Whether to skip any cached file contents or reload the whole file.

    Return the oblique strategy
    """
    strategies = _load(strategies_file, skip_cache)
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
