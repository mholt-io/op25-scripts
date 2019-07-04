#! /bin/sh
~/op25/op25/gr-op25_repeater/apps/rx.py --args 'rtl' -N 'LNA:49' -S 2400000 -o 25000 -l http:0.0.0.0:8888 -q -1 -T ici-trunk.tsv -V -2 -U 2> stderr.2
