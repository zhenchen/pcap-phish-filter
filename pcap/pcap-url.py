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


import string

pcap_url_referer = open('pcap-url-referer', 'r')

pcap_url = open('pcap-url', 'w')

line = 'hello world'

while line != '':
    line = pcap_url_referer.readline().replace('\n','')
    if len(string.split(line)) == 2:
        word1, word2 = string.split(line)
        if word1 == 'Referer:':
            pcap_url.write(word2 + '\n')
            print word2

pcap_url_referer.close()

pcap_url.close()




