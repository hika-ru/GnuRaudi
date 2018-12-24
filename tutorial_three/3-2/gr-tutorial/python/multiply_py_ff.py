#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2018 gr-tutorial author.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class multiply_py_ff(gr.sync_block):    # This class is a child
                                        # to class gr.sync_block
    """
    docstring for block multiply_py_ff
    """
    def __init__(self, multiple):
        self.multiple = multiple # Specific init for this very class.
        #Run standard init function for object of type sync_block
        gr.sync_block.__init__(self,
            name="multiply_py_ff",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])

    # The work function is where the actual processing happens, where
    # we want our code to be.
    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        out[:] = self.multiple * in0
        return len(output_items[0])

