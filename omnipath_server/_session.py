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

import functools as _ft

from pypath_common import log as _read_log, session as _session

_get_session = _ft.partial(_session, "omnipath_server")
log = _ft.partial(_read_log, "omnipath_server")

session = _get_session()
_log = session._logger.msg
