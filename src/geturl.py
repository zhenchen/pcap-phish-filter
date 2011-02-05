#!/usr/bin/python

#  Copyright (C) 2011 Tianyang Li
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#  Author Tianyang Li
#  E-Mail tmy1018 gmail com

"""
A module for checking URL's found in a pcap file for phishing
"""

import sys

import pcap

def check_url(URL):

if __name__ == "__main__":
    if sys.argv[1] != '':
        sys.exit(0)
    else:
        print 'No pcap file is provided. Won\'t check for phishing!\n'
        print 'Usage: checkurl.py <pcap file>'
        sys.exit(0)
