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


import sys, os

import client


class CheckURL:
    def GetAPIKey(self):
        """
        Google API key is located in file 'api-key'
        """
        try:
            fin = open('api-key', 'r')
        except IOError:
            print 'Unable to find \'api-key\' file containing the API key'
            sys.exit(0)
        else:
            self._api_key = fin.readline().replace('\n','')
            fin.close()
    
    
    def __init__(self):
        self.GetAPIKey()

        
    def CheckForURL(self):
        client.CheckForUrl(self._api_key)
        
        

def main():
    pf = CheckURL()
    pf.CheckForURL()
    sys.exit(0)
        
        
if __name__ == "__main__":
    main()

