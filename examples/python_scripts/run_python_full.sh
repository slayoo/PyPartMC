#!/bin/sh
for i in 10 100 1000 10000
do
  time python timing_run_full.py $i
done
