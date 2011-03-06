#!/bin/bash

time_beg=`date`

tcptrace -ne --output_dir=extract class_all_*

time_fin_tcptrace=`date`

grep -h 'Referer: http://' ./extract/a* > pcap-url-referer
grep -h 'Referer: http://' ./extract/b* > pcap-url-referer
grep -h 'Referer: http://' ./extract/c* > pcap-url-referer
grep -h 'Referer: http://' ./extract/d* > pcap-url-referer
grep -h 'Referer: http://' ./extract/e* > pcap-url-referer
grep -h 'Referer: http://' ./extract/f* > pcap-url-referer
grep -h 'Referer: http://' ./extract/g* > pcap-url-referer
grep -h 'Referer: http://' ./extract/h* > pcap-url-referer
grep -h 'Referer: http://' ./extract/i* > pcap-url-referer
grep -h 'Referer: http://' ./extract/j* > pcap-url-referer
grep -h 'Referer: http://' ./extract/k* > pcap-url-referer
grep -h 'Referer: http://' ./extract/l* > pcap-url-referer
grep -h 'Referer: http://' ./extract/m* > pcap-url-referer
grep -h 'Referer: http://' ./extract/n* > pcap-url-referer
grep -h 'Referer: http://' ./extract/o* > pcap-url-referer
grep -h 'Referer: http://' ./extract/p* > pcap-url-referer
grep -h 'Referer: http://' ./extract/q* > pcap-url-referer
grep -h 'Referer: http://' ./extract/r* > pcap-url-referer
grep -h 'Referer: http://' ./extract/s* > pcap-url-referer
grep -h 'Referer: http://' ./extract/t* > pcap-url-referer
grep -h 'Referer: http://' ./extract/u* > pcap-url-referer
grep -h 'Referer: http://' ./extract/v* > pcap-url-referer
grep -h 'Referer: http://' ./extract/w* > pcap-url-referer
grep -h 'Referer: http://' ./extract/x* > pcap-url-referer
grep -h 'Referer: http://' ./extract/y* > pcap-url-referer
grep -h 'Referer: http://' ./extract/z* > pcap-url-referer

time_fin_grep_referer=`date`

./pcap-url.py

time_fin_grep_URL=`date`

echo "Start ${time_beg}"
echo "pcap extraction finished ${time_fin_tcptrace}"
echo "grep refere finished ${time_fin_grep_referer}"
echo "URL extraction finished ${time_fin_grep_URL}"



