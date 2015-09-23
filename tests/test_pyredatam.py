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
import queries


class RedatamTestCase(unittest.TestCase):

    def test_arealist_query(self):

        # Test case AREALIST1
        area_level = "FRAC"
        variables = "PERSONA.CONDACT"

        area_filter = {"PROV": ["02", "03"]}
        universe_filter = "1 = 1"
        title = "El titulo"

        query = pyredatam.arealist_query(area_level, variables, area_filter,
                                         universe_filter, title)
        self.assertEqual(query, queries.AREALIST1.strip())

        # Test case AREALIST2
        variables = ["PERSONA.CONDACT"]
        query = pyredatam.arealist_query(area_level, variables)
        self.assertEqual(query, queries.AREALIST2.strip())

        # Test case AREALIST3
        area_filter = {"PROV": "02"}
        query = pyredatam.arealist_query(area_level, variables, area_filter)
        self.assertEqual(query, queries.AREALIST3.strip())

    def test_counter_query(self):

        # Test case COUNTER1
        area_level = "RADIO"
        entity_count = "PERSONA"

        area_filter = {"PROV": "02"}
        universe_filter = "1 = 1"
        title = "El titulo"

        query = pyredatam.counter_query(area_level, entity_count, area_filter,
                                        universe_filter, title)
        self.assertEqual(query, queries.COUNTER1.strip())

        # Test case COUNTER2
        area_level = "DPTO"
        entity_count = "FRAC"
        incl_area_name = True
        incl_total = True
        query = pyredatam.counter_query(area_level, entity_count, area_filter,
                                        universe_filter, title, incl_area_name,
                                        incl_total)
        self.assertEqual(query, queries.COUNTER2.strip())

    def test_median_query(self):

        # Test case MEDIAN1
        variable = "PERSONA.P03"
        by_var1 = "PERSONA.CONDACT"
        by_var2 = "PERSONA.P02"
        incl_name = True
        area_break = "PROV"

        area_filter = None
        universe_filter = "1 = 1"
        title = "El titulo"

        query = pyredatam.median_query(variable, by_var1, by_var2, incl_name,
                                       area_break, area_filter,
                                       universe_filter, title)
        self.assertEqual(query, queries.MEDIAN1.strip())

        # Test case MEDIAN2
        variable = "PERSONA.P03"
        incl_name = None
        area_break = None

        universe_filter = None
        title = None
        query = pyredatam.median_query(variable, by_var1, by_var2, incl_name,
                                       area_break, area_filter,
                                       universe_filter, title)
        self.assertEqual(query, queries.MEDIAN2.strip())

        # Test case MEDIAN3
        variable = "PERSONA.P03"
        by_var1 = None
        by_var2 = None
        query = pyredatam.median_query(variable, by_var1, by_var2, incl_name,
                                       area_break, area_filter,
                                       universe_filter, title)
        self.assertEqual(query, queries.MEDIAN3.strip())


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
