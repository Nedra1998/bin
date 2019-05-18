#!/bin/bash

COUNT="-10"
if [[ ! -z "$1" ]]; then
  COUNT="-$1"
fi

du -hs * | sort -rh | head "$COUNT"
