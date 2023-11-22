#!/bin/bash

for i in 10 100 1000 10000
do
  echo -n $i " "
  { time -p python timing_run_full.py $i; } 3>&1 1>&2 2>&3 | fgrep user | cut -d' ' -f2
done
