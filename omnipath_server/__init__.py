#!/usr/bin/env python

#
# This file is part of the `omnipath_server` Python module
#
# Copyright 2024
# Heidelberg University Hospital
#
# File author(s): OmniPath Team (omnipathdb@gmail.com)
#
# Distributed under the GPLv3 license
# See the file `LICENSE` or read a copy at
# https://www.gnu.org/licenses/gpl-3.0.txt
#

"""
OmniPath HTTP server based on Twisted
"""

__all__ = [
    "__version__",
    "__author__",
]

from ._metadata import __author__, __version__
from ._session import _log, log, session
