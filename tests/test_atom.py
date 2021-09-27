#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Unit Test convert Atom Entry

"""
__author__ = 'Frederic Laurent'
__version__ = "1.0"
__copyright__ = 'Copyright 2017, Frederic Laurent'
__license__ = "MIT"

import os.path
import re
import unittest

from lxml import etree
import io
from atomtorss2 import xslt_ext
from atomtorss2 import atom1_to_rss2_xslpy

class PrefixResolver(etree.Resolver):
    def __init__(self, rootdir, *args, **kwargs):
        super(PrefixResolver, self).__init__(*args, **kwargs)
        self.rootdir = rootdir
        self.prefix = "file://"

    def resolve(self, url, pubid, context):
        if url.startswith(self.prefix):
            fname = os.path.join(self.rootdir, url[len(self.prefix):])
            print("new : %s" % fname)
            with open(fname, "r") as fin:
                data = fin.read()
                data = re.sub('select="format-dateTime\(.*?"', 'select="."', data)

                return self.resolve_string(data, context)


class TestXSLT(unittest.TestCase):
    def test_transform_atom_include_resolver(self):
        filedir = os.path.dirname(os.path.abspath(__file__))
        filedirxsl = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'atomtorss2'))

        xml1_fn = os.path.join(filedir, 'atom_instance.xml')

        # Process
        _parser = etree.XMLParser()
        _parser.resolvers.add(PrefixResolver(filedirxsl))

        xslt = etree.parse(os.path.join(filedirxsl, 'atom1_to_rss2_pyext.xsl'), _parser)
        proc = xslt_ext.DateFormatterProcessor(xslt)
        result_xml = proc.transform(etree.parse(xml1_fn))

        # check
        xmlexpected_fn = os.path.join(filedir, 'rss2_from_xslt1_expected.xml')
        xml2 = etree.parse(xmlexpected_fn)

        self.assertEqual(etree.tostring(result_xml, encoding='UTF-8', pretty_print=True, xml_declaration=True),
                         etree.tostring(xml2, encoding='UTF-8', pretty_print=True, xml_declaration=True))


    def test_transform_atom_include_sample(self):
        filedir = os.path.dirname(os.path.abspath(__file__))
        filedirxsl = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'atomtorss2'))
        print(f" DIR XSL {filedirxsl}")
        xml1_fn = os.path.join(filedir, 'atom_instance.xml')

        # Process
        xslt = etree.parse(os.path.join(filedirxsl, 'atom1_to_rss2_pyext.xsl'))
        print(f" >>> {os.path.join(filedirxsl, 'atom1_to_rss2_pyext.xsl')}")
        print(f" >>> {xslt}")

        proc = xslt_ext.DateFormatterProcessor()
        proc.load_xslt(os.path.join(filedirxsl, 'atom1_to_rss2_pyext.xsl'))
        result_xml = proc.transform(etree.parse(xml1_fn))

        # check
        xmlexpected_fn = os.path.join(filedir, 'rss2_from_xslt1_expected.xml')
        xml2 = etree.parse(xmlexpected_fn)

        self.assertEqual(etree.tostring(result_xml, encoding='UTF-8', pretty_print=True, xml_declaration=True),
                         etree.tostring(xml2, encoding='UTF-8', pretty_print=True, xml_declaration=True))


    def test_transform_atom_nofile(self):
        filedir = os.path.dirname(os.path.abspath(__file__))
        xml1_fn = os.path.join(filedir, 'atom_instance.xml')

        # Process
        #txt = bytes(bytearray(atom1_to_rss2_xslpy.xslt, encoding='utf-8'))
        xslt = etree.parse(io.StringIO(atom1_to_rss2_xslpy.xslt))
        #xslt = etree.parse(txt)

        proc = xslt_ext.DateFormatterProcessor(xslt)
        result_xml = proc.transform(etree.parse(xml1_fn))

        # check
        xmlexpected_fn = os.path.join(filedir, 'rss2_from_xslt1_expected.xml')
        xml2 = etree.parse(xmlexpected_fn)

        self.assertEqual(etree.tostring(result_xml, encoding='UTF-8', pretty_print=True, xml_declaration=True),
                         etree.tostring(xml2, encoding='UTF-8', pretty_print=True, xml_declaration=True))


if __name__ == '__main__':
    unittest.main()
