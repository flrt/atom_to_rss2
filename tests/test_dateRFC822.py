#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Unit Test Date format converter for ElementTree XSLT

"""
__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import unittest
from atomtorss2 import etree_formatdt


class TestDateFRC822(unittest.TestCase):
    def test_convert(self):
        conv = etree_formatdt

        date_in = "2017-11-03T16:55:03.198512+00:00"
        date_out = conv.convert(date_in)
        date_out_expected = "Fri, 03 Nov 2017 16:55:03 +0000"

        self.assertEqual(date_out_expected, date_out)


if __name__ == '__main__':
    unittest.main()
