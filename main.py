#!/usr/bin/env python
# Copyright (c) 2017, Nathan Lopez
# Stitch is under the MIT license. See the LICENSE file at the root of the project for the detailed license terms.

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Application'))

from Application.stitch_cmd import *

server_main()
