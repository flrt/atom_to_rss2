#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Unit Test extension function

"""
__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import unittest
from lxml import etree
from atomtorss2 import xslt_ext
import os.path


class TestXSLT(unittest.TestCase):
    def test_transform_fromstring(self):
        xslt_src = u"""
        <xsl:stylesheet 
            xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
            xmlns:pyext="http://www.opikanoba.org/ns/etree-extensions"
            exclude-result-prefixes="pyext"
            extension-element-prefixes="pyext"
            version="1.0">
        
            <xsl:template match="/test">
                <pubDate>
                    <xsl:apply-templates select="isodate" mode="RFC822"/>
                </pubDate>
            </xsl:template>

            <xsl:template match="isodate" mode="RFC822">
                <pyext:formatdt></pyext:formatdt>
            </xsl:template>
        </xsl:stylesheet>
        """

        xml_src = u"""<?xml version="1.0" ?><test><isodate>2017-11-03T16:55:03.198512+00:00</isodate></test>"""
        expected_result = u"""<?xml version="1.0" ?><pubDate>Fri, 03 Nov 2017 16:55:03 +0000</pubDate>"""

        # Process
        proc = xslt_ext.DateFormatterProcessor(etree.fromstring(xslt_src))
        result_xml = proc.transform(etree.fromstring(xml_src))

        # Check result
        xml2 = etree.fromstring(expected_result)
        self.assertEqual(etree.tostring(result_xml), etree.tostring(xml2))

    def test_transform_fromfile(self):
        filedir = os.path.dirname(os.path.abspath(__file__))
        xml1_fn = os.path.join(filedir, 'simple_instance.xml')

        # Process
        xslt = etree.parse(os.path.join(filedir, 'simple_ext.xsl'))
        proc = xslt_ext.DateFormatterProcessor(xslt)

        result_xml = proc.transform(etree.parse(xml1_fn))

        # Check result
        expected_result = u"""<?xml version="1.0" ?><pubDate>Fri, 03 Nov 2017 16:55:03 +0000</pubDate>"""

        xml2 = etree.fromstring(expected_result)
        self.assertEqual(etree.tostring(result_xml), etree.tostring(xml2))

    def test_transform_none(self):
        filedir = os.path.dirname(os.path.abspath(__file__))
        xml1_fn = os.path.join(filedir, 'simple_instance.xml')

        # Process
        proc = xslt_ext.DateFormatterProcessor()

        result_xml = proc.transform(etree.parse(xml1_fn))

        # Check result
        self.assertIsNone(result_xml)


if __name__ == '__main__':
    unittest.main()
