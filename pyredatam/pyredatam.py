#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
pyredatam.py

Redatam object created from a .dic file that generate queries.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement


def arealist_query(area_level, variables, area_filter=None,
                   universe_filter=None, title=None):
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

    lines = ["RUNDEF Job"]

    if area_filter:
        lines.append("    SELECTION INLINE,")

        area_type = area_filter.keys()[0]
        areas = area_filter.values()[0]
        if type(areas) != list:
            areas = [areas]

        lines.append("     {} {}".format(area_type, ", ".join(areas)))

    if universe_filter:
        lines.append("    UNIVERSE " + universe_filter)

    lines.append("")
    lines.append("TABLE TABLE1")

    if title:
        lines.append('    TITLE "' + title + '"')

    lines.append("    AS AREALIST")

    if type(variables) != list:
        variables = [variables]
    lines.append("    OF {}, {}".format(area_level, ", ".join(variables)))

    return "\n".join(lines)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
