#!/bin/bash

time_partmc () {
  echo -n $1 " "
  { time -p ../../../gitmodules/partmc/build/partmc urban_plume_$1.spec; } 3>&1 1>&2 2>&3 | fgrep user | cut -d' ' -f2
}

time_partmc 10
time_partmc 100
time_partmc 1000
time_partmc 10000
