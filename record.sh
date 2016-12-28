#!/bin/bash

dir=~/Desktop/video.h264
ms=$(($1*1000))
time=''

if [ $# -eq 1 ]; then 
	time='-t '$ms;
fi

echo recording $1 seconds to $dir 

raspivid -o $dir -w 1280 -h 720 -b 8000000 $time
