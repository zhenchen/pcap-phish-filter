#!/bin/bash

tcptrace -ne --output_dir=extract *.pcap

grep -h 'Referer: http://' ./extract/[a-d]* > pcap-url-referer
grep -h 'Referer: http://' ./extract/[e-j]* > pcap-url-referer
grep -h 'Referer: http://' ./extract/[k-n]* > pcap-url-referer
grep -h 'Referer: http://' ./extract/[o-t]* > pcap-url-referer
grep -h 'Referer: http://' ./extract/[u-z]* > pcap-url-referer

./pcap-url.py




