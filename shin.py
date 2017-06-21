#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
from __future__ import division
import os
import sys
import re

# Assumes SolidPython is in site-packages or elsewhwere in sys.path
from solid import *
from solid.utils import *

SEGMENTS = 48


foot_radius = 30
foot_height = 30
leg_base_diameter = 15
leg_upper_diameter = 25

def foot():
    f = sphere(foot_radius)

    return f

def assembly():
    # Your code here!
    a = foot() + up(foot_height)(foot())

    return a

if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=True)
