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

foot_radius = 25
foot_height = foot_radius * 2 + 10
leg_base_diameter = 15
leg_upper_diameter = 20
leg_length = 200


def foot():
    f = sphere(foot_radius) + cylinder(leg_base_diameter, foot_height, 0)
    f = hull()(f)

    return f


def shin():
    s = cylinder(leg_upper_diameter, leg_length, leg_base_diameter)

    return s


def knee_joint():
    joint_width = 40
    joint_height = 20
    bearing_outer = 21
    # bearing_inner = 8
    bearing_width = 7
    # spammyheight = 20

    # joint base
    j = up(2.5)(
        cube([joint_width, joint_width, 5], True))
    # Left and right bearing tabs
    j += right(joint_width / 2 - bearing_width / 2)(
        up((joint_height + bearing_outer / 2 + 5) / 2)(
            cube([bearing_width, joint_width, joint_height + bearing_outer / 2 + 5], True)))

    j += left(joint_width / 2 - bearing_width / 2)(
        up((joint_height + bearing_outer / 2 + 5) / 2)(
            cube([bearing_width, joint_width, joint_height + bearing_outer / 2 + 5], True)))

    # Cut bearing slots
    j -= up(joint_height)(
        rotate([0, 90, 0])(
            cylinder(bearing_outer/2, joint_width + 20, center=True)))

    return j


def assembly():
    # Your code here!
    # a = foot() + up(foot_height-foot_radius)(shin())
    a = knee_joint()

    return a


if __name__ == '__main__':
    a = assembly()
    scad_render_to_file(a, file_header='$fn = %s;' % SEGMENTS, include_orig_code=True)
    print(scad_render(a))
