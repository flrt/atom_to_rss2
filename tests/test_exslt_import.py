#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Unit Test XSL import

"""
__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import os.path
import unittest

from lxml import etree

from atomtorss2 import xslt_ext


class PrefixResolver(etree.Resolver):
    def __init__(self, rootdir, *args, **kwargs):
        super(PrefixResolver, self).__init__(*args, **kwargs)
        self.rootdir = rootdir
        self.prefix = "file://"

    def resolve(self, url, pubid, context):
        if url.startswith(self.prefix):
            print("Resolved url %s " % url)
            print("new : %s" % os.path.join(self.rootdir, url[len(self.prefix):]))

            return self.resolve_filename(os.path.join(self.rootdir, url[len(self.prefix):]), context)


class TestXSLT(unittest.TestCase):
    def test_transform_fromfile(self):
        filedir = os.path.dirname(os.path.abspath(__file__))
        xml1_fn = os.path.join(filedir, 'simple_instance.xml')

        # Process
        _parser = etree.XMLParser()
        _parser.resolvers.add(PrefixResolver(filedir))

        xslt = etree.parse(os.path.join(filedir, 'simple_ext_1.xsl'), _parser)
        proc = xslt_ext.DateFormatterProcessor(xslt)

        result_xml = proc.transform(etree.parse(xml1_fn))

        # Check result
        expected_result = u"""<?xml version="1.0" ?><pubDate>Fri, 03 Nov 2017 16:55:03 +0000</pubDate>"""

        print(etree.tostring(result_xml, pretty_print=True, xml_declaration=True))

        xml2 = etree.fromstring(expected_result)
        self.assertEqual(etree.tostring(result_xml), etree.tostring(xml2))

    def test_transform_fromfile_ns(self):
        filedir = os.path.dirname(os.path.abspath(__file__))
        xml1_fn = os.path.join(filedir, 'simple_instance2.xml')

        # Process
        _parser = etree.XMLParser()
        _parser.resolvers.add(PrefixResolver(filedir))

        xslt = etree.parse(os.path.join(filedir, 'simple_ext_3.xsl'), _parser)
        proc = xslt_ext.DateFormatterProcessor(xslt)

        result_xml = proc.transform(etree.parse(xml1_fn))
        print(etree.tostring(result_xml, pretty_print=True, xml_declaration=True))

        # Check result
        expected_result = u"""<?xml version="1.0" ?><pubDate>Fri, 03 Nov 2017 16:55:03 +0000</pubDate>"""

        xml2 = etree.fromstring(expected_result)
        self.assertEqual(etree.tostring(result_xml), etree.tostring(xml2))


if __name__ == '__main__':
    unittest.main()
