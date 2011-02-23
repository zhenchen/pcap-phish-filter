#!/bin/bash

tcptrace -ne --output_dir=extract *.pcap

grep -h 'Referer: http://' extract/* > pcap-url-referer

./pcap-url.py




