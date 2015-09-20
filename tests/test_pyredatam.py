#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyredatam

Tests for `pyredatam` module.
"""

from __future__ import unicode_literals
import unittest
import nose

import pyredatam

QUERY_AREALIST1 = """
RUNDEF Job
    SELECTION INLINE,
     PROV 02, 03
    UNIVERSE 1 = 1

TABLE TABLE1
    TITLE "El titulo"
    AS AREALIST
    OF FRAC, PERSONA.CONDACT
""".strip()

QUERY_AREALIST2 = """
RUNDEF Job

TABLE TABLE1
    AS AREALIST
    OF FRAC, PERSONA.CONDACT
""".strip()

QUERY_AREALIST3 = """
RUNDEF Job
    SELECTION INLINE,
     PROV 02

TABLE TABLE1
    AS AREALIST
    OF FRAC, PERSONA.CONDACT
""".strip()


class RedatamTestCase(unittest.TestCase):

    def test_arealist_query(self):

        area_level = "FRAC"
        variables = "PERSONA.CONDACT"
        area_filter = {"PROV": ["02", "03"]}
        universe_filter = "1 = 1"
        title = "El titulo"

        query = pyredatam.arealist_query(area_level, variables, area_filter,
                                         universe_filter, title)
        self.assertEqual(query, QUERY_AREALIST1)

        variables = ["PERSONA.CONDACT"]
        query = pyredatam.arealist_query(area_level, variables)
        self.assertEqual(query, QUERY_AREALIST2)

        area_filter = {"PROV": "02"}
        query = pyredatam.arealist_query(area_level, variables, area_filter)
        self.assertEqual(query, QUERY_AREALIST3)

if __name__ == '__main__':
    nose.run(defaultTest=__name__)
