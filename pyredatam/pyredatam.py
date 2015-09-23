#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyredatam.py

Redatam object created from a .dic file that generate queries.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement


# PUBLIC
def arealist_query(area_level, variables, area_filter=None,
                   universe_filter=None, title=None, incl_area_name=False):
    """Generate an Area List REDATAM query.

    Args:
        area_level (str): Level of geographical area of the list.
        variables (str or list): Variable/s that will be asked for their data.
        area_filter (str or list): Geographical area/s where results are asked.
        universe_filter (str): REDATAM filter exrpession.
        title (str): Title of the results table.

    Returns:
        str: REDATAM query ready to paste in a processor.

    >>> print(arealist_query("FRAC", "PERSONA.CONDACT",
    ...                      {"PROV": ["02", "03"]}))
    RUNDEF Job
        SELECTION INLINE,
         PROV 02, 03
    <BLANKLINE>
    TABLE TABLE1
        AS AREALIST
        OF FRAC, PERSONA.CONDACT
    """

    # RUNDEF section
    lines = _build_rundef_section(area_filter, universe_filter)

    # TABLE section
    lines.append("TABLE TABLE1")
    lines.extend(_build_title(title))
    lines.append("    AS AREALIST")
    lines.append(_build_of_variables(area_level, variables, incl_area_name))

    return "\n".join(lines)


def counter_query(area_level, entity_count, area_filter=None,
                  universe_filter=None, title=None, incl_area_name=False,
                  incl_total=False):
    """Generate an Area List REDATAM query where entities are counted.

    Args:
        area_level (str): Level of geographical area of the list.
        entity_count (str): Entity whose instances are to be counted.
        area_filter (str or list): Geographical area/s where results are asked.
        universe_filter (str): REDATAM filter exrpession.
        title (str): Title of the results table.
        incl_area_name (bool): True to include area level name besides code.
        incl_total (bool): True to include a total at the end of the table.

    Returns:
        str: REDATAM query ready to paste in a processor.
    """

    # RUNDEF section
    lines = _build_rundef_section(area_filter, universe_filter)

    # DEFINE section
    new_variable = area_level + ".COUNTER"
    lines.append("DEFINE " + new_variable)
    lines.append("    AS COUNT " + entity_count)
    lines.append("    TYPE INTEGER")
    lines.append("")

    # TABLE section
    lines.append("TABLE TABLE1")
    lines.extend(_build_title(title))
    lines.append("    AS AREALIST")
    lines.append(_build_of_variables(area_level, [new_variable],
                                     incl_area_name))

    lines.extend(["    TOTAL"] if incl_total else [])

    return "\n".join(lines)


def median_query(variable, by_var1=None, by_var2=None, incl_name=None,
                 area_break=None, area_filter=None, universe_filter=None,
                 title=None):
    """Generate a median of a variable REDATAM query.

    Args:
        variable (str): Variable which mean is to be taken..
        by_var1 (str): Variable to open the result in categories.
        by_var2 (str): Cross variable to open result again, like a pivot table.
        incl_name (str): Include descriptions besides codes.
        area_break (str): Geographical entity to break the result with.
        area_filter (str or list): Geographical area/s where results are asked.
        universe_filter (str): REDATAM filter exrpession.
        title (str): Title of the results table.

    Returns:
        str: REDATAM query ready to paste in a processor.
    """

    # RUNDEF section
    lines = _build_rundef_section(area_filter, universe_filter)

    # TABLE section
    lines.append("TABLE TABLE1")
    lines.extend(_build_title(title))
    lines.append("    AS MEDIAN")
    lines.append("    OF " + variable)
    lines.extend(["        BY " + by_var1] if by_var1 else [])
    lines.extend(["        BY " + by_var2] if by_var2 else [])
    lines.extend(["        COMPLETENAME"] if incl_name else [])
    lines.extend(_build_area_break(area_break))

    return "\n".join(lines)


def mean_query():
    pass


def cross_query():
    pass


def frequencies_query():
    pass


def stats_query():
    pass


# PRIVATE
def _build_rundef_section(area_filter, universe_filter):
    lines = ["RUNDEF Job"]
    lines.extend(_build_area_filter(area_filter))
    lines.extend(_build_universe_filter(universe_filter))
    lines.append("")
    return lines


def _build_area_filter(area_filter):
    lines = []

    if area_filter:
        lines.append("    SELECTION INLINE,")

        area_type = area_filter.keys()[0]
        areas = area_filter.values()[0]
        if type(areas) != list:
            areas = [areas]

        lines.append("     {} {}".format(area_type, ", ".join(areas)))

    return lines


def _build_universe_filter(universe_filter):
    return ["    UNIVERSE " + universe_filter] if universe_filter else []


def _build_title(title):
    return ['    TITLE "' + title + '"'] if title else []


def _build_area_break(area_break):
    return ['    AREABREAK ' + area_break] if area_break else []


def _build_of_variables(area_level, variables, incl_area_name):
    if type(variables) != list:
        variables = [variables]
    if incl_area_name:
        variables.insert(0, area_level + ".NOM" + area_level)
    return "    OF {}, {}".format(area_level, ", ".join(variables))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
