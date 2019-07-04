#!/bin/bash


BASEPATH=`dirname $0`
RXDIR="/home/pi/op25/op25/gr-op25_repeater/apps/"
ERRORLOG=`readlink -f $BASEPATH/op25_error.log`
OP25_ARGS="rtl"
OP25_GAIN="lna:40"
#OP25_SAMPLERATE="2400000"
OP25_SAMPLERATE="960000"
OP25_PPM="-0.5"
OP25_DEMOD="cqpsk"
#OP25_OFFSET="12.5e3"
OP25_OFFSET="0"
TRUNKCONFIG=`readlink -f $BASEPATH/ici-home.tsv`

cd /home/pi/op25/op25/gr-op25_repeater/apps/
./rx.py --args $OP25_ARGS --gains $OP25_GAIN -q $OP25_PPM -S $OP25_SAMPLERATE -D $OP25_DEMOD -2 -o $OP25_OFFSET -T $TRUNKCONFIG -w -U -l http:0.0.0.0:8888
#cat $ERRORLOG
