#!/usr/bin/env python
#vim: fileencoding=utf-8

from __future__ import print_function, division, unicode_literals
from os.path import dirname, abspath, isdir
import unittest
import sys
import argparse

import pep8
import xmlrunner

CURRENT_DIR = dirname(abspath(__file__))
sys.path.insert(0, CURRENT_DIR)


class TestPEP8(unittest.TestCase):
    def test_pep8(self):
        arglist = [
                '--statistics',
                '--filename=*.py',
                '--show-source',
                '--repeat',
                CURRENT_DIR,
                ]
        options, args = pep8.process_options(arglist)
        runner = pep8.input_file

        for path in args:
            if isdir(path):
                pep8.input_dir(path, runner=runner)
            elif not pep8.excluded(path):
                options.counters['files'] += 1
                runner(path)

        pep8.print_statistics()
        errors = pep8.get_count('E')
        warnings = pep8.get_count('W')
        message = 'pep8: {0} errors / {1} warnings'.format(errors, warnings)
        self.assertEqual(errors, warnings, message)


def make_suite(pattern, pep8_flg):
    suite = unittest.defaultTestLoader.discover(CURRENT_DIR, pattern=pattern)
    if pep8_flg:
        pep8test = unittest.defaultTestLoader.loadTestsFromTestCase(TestPEP8)
        suite.addTest(pep8test)
    return suite


if __name__ == '__main__':
    # parse command line options
    parser = argparse.ArgumentParser(description='Run testsuite')
    parser.add_argument('--report', action='store_true')
    parser.add_argument('--without-pep8', action='store_false')
    parser.add_argument('--pattern', type=str, default='test*.py')
    args = parser.parse_args()
    suite = make_suite(args.pattern, args.without_pep8)
    if args.report:
        xmlrunner.XMLTestRunner(verbose=1, output='test_reports').run(suite)
    else:
        unittest.TextTestRunner(verbosity=2).run(suite)
