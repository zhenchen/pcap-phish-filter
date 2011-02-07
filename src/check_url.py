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
A module for checking URL using Google Safe Browsing
"""

__author__ = 'Tianyang Li <tmy1018 at gmail.com>'
__copyright__ = 'Copyright (c) 2011 Tianyang Li'
__license__ = 'GPLv3'
__url__ = 'http://code.google.com/p/pcap-phish-filter/'
__version__ = '0.0'

import sys

def check_url(URL):
    return True

if __name__ == "__main__":
    if sys.argv[1] != '':
        if check_url(sys.argv[1]) == True:
            print 'This is a phishing site!'
        else:
            print 'This is not a phishing site.'
        sys.exit(0)
    else:
        print 'No URL is provided. Won\'t check for phishing!\n'
        + 'Usage: checkurl.py <URL>\n'
        sys.exit(0)
