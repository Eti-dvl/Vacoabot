#!/bin/bash
rpiv=`uname -a | awk '{print $4}'`
python /home/pi/rpibot/tweet.py "Ma version de Raspbian est la $rpiv"
