#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
utils.py

Helper methods.
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import os


def get_data_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "data"))
