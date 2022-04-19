#!/usr/bin/env python
#
# Copyright (C) 2013 Christian Brandt
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#  
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from os.path import *
from os import rename
from sys import argv

def change_content(change_to, dirname, names):
    for name in names:
        full_path = join(dirname, name)
        if isfile(full_path):
            print "Adjusting content in %s" % full_path
            content = open(full_path, "r").read()
            content = content.replace(change_from.capitalize(), change_to.capitalize())
            content = content.replace(change_from.upper(), change_to.upper())
            content = content.replace(change_from, change_to)
            open(full_path, "w").write(content)
        elif isdir(full_path):
            walk(full_path, change_content, change_to)

def rename_files(change_to, dirname, names):
    for name in names:
        full_path = join(dirname, name)
        if isdir(full_path):
            walk(full_path, rename_files, change_to)
        if name.find(change_from) != -1:
            new_name = name.replace(change_from, change_to)
            print "Renaming %s to %s" % (full_path, join(dirname, new_name))
            rename(full_path, join(dirname, new_name))

change_from = 'fd_toolkit'
change_to = argv[-1].lower()
print "Changing name of toolkit project to '%s'." % change_to
walk(".", change_content, change_to)
walk(".", rename_files, change_to)
