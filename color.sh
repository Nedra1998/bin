#!/bin/bash

if [ "$1" == "" ] || [ "$1" == "fg" ]; then
  for i in {30..37}; do
    printf "\e[${i}m%.3i\e[0m " $i
  done
  printf "\n"
elif [ "$1" == "bg" ]; then
  for i in {40..47}; do
    printf "\e[${i}m%.3i\e[0m " $i
  done
  printf "\n"
elif [ "$1" == "256" ]; then
  if [ "$2" == "" ] || [ "$2" == "fg" ]; then
    for i in {0..255}; do
      if [[ $(( i % 32 )) -eq 0 ]] && [[ $i -ne 0 ]]; then
        printf "\n"
      fi
      printf "\e[38;5;${i}m%.3i\e[0m " $i
    done
  elif [ "$2" == "bg" ]; then
    for i in {0..255}; do
      if [[ $(( i % 32 )) -eq 0 ]] && [[ $i -ne 0 ]]; then
        printf "\n"
      fi
      printf "\e[48;5;${i}m%.3i\e[0m " $i
    done
  fi
  printf "\e[0m\n"
fi
