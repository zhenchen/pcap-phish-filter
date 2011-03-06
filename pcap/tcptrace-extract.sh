#!/bin/bash

time_beg=`date`

tcptrace -ne --output_dir=extract class_all_*

time_fin_tcptrace=`date`

grep -h 'Referer: http://' ./extract/[a-d]* > pcap-url-referer
grep -h 'Referer: http://' ./extract/[e-j]* > pcap-url-referer
grep -h 'Referer: http://' ./extract/[k-n]* > pcap-url-referer
grep -h 'Referer: http://' ./extract/[o-t]* > pcap-url-referer
grep -h 'Referer: http://' ./extract/[u-z]* > pcap-url-referer

time_fin_grep_referer=`date`

./pcap-url.py

time_fin_grep_URL=`date`

echo "Start ${time_beg}"
echo "pcap extraction finished ${time_fin_tcptrace}"
echo "grep refere finished ${time_fin_grep_referer}"
echo "URL extraction finished ${time_fin_grep_URL}"



