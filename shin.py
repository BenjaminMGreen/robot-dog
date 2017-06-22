#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

SEGMENTS = 32


foot_radius = 20
foot_height = 50
leg_base_diameter = 15
leg_upper_diameter = 25
leg_length = 150

def foot():
    f = sphere(foot_radius) + cylinder(leg_base_diameter, foot_height - foot_radius)
    f = hull()(f)

    return f

def assembly():
    # Your code here!
    a = foot()

    return a

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=True)
    print(scad_render(a))
