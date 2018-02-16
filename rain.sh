#!/bin/bash

VERSION=0.0

resize() {
  w=$(tput cols) h=$(tput lines)
}

sets=(
  "||"
  "│┃"
)

f=75
w=80 h=24

RNDSTART=0
OPTIND=1
COLOR=39
NOLENGTH=0
resize
((d=w/4))
s=1

while getopts "c:d:s:Lhv" arg; do
  case $arg in
    c) COLOR=$OPTARG;;
    d) ((d=(OPTARG>=0)?OPTARG:d));;
    s) ((s=(OPTARG>1 && OPTARG<11)?OPTARG:s));;
    L) NOLENGTH=1;;
    h) echo -e "Usage: $(basename $0) [OPTION]..."
       echo -e "Animated rain terminal screensaver.\n"
       echo -e " -c\t\tColor of rain."
       echo -e " -d\t\tNumber of drops."
       echo -e " -s\t\tMinimum speed of drops."
       echo -e " -L\t\tEnables long drops."
       exit;;
    v) echo "$(basename -- "$0") $VERSION"
       exit 0;;
  esac
done

cleanup() {
  read -t 0.001 && cat </dev/stdin>/dev/null

  ((FORCE_RESET)) && reset && exit 0

  tput rmcup
  tput cnorm
  stty echo
  echo -ne "\033[0m"
  exit 0
}

trap resize SIGWINCH
trap cleanup HUP TERM
trap 'break 2' INT

stty -echo
tput smcup || FORCE_RESET=1
tput civis
tput clear

for (( i=1; i<=d; i++ )); do
  ((x[i]=RANDOM*w/32768))
  ((y[i]=RANDOM*2*h/32768-2*h))
  ((v[i]=RANDOM*3/32768+s))
  ((e[i]=y[i]-v[i]))
done

if [[ $COLOR == "red" ]]; then
  echo -ne "\033[31m"
elif [[ $COLOR == "green" ]]; then
  echo -ne "\033[32m"
elif [[ $COLOR == "yellow" ]]; then
  echo -ne "\033[33m"
elif [[ $COLOR == "blue" ]]; then
  echo -ne "\033[34m"
elif [[ $COLOR == "magenta" ]]; then
  echo -ne "\033[35m"
elif [[ $COLOR == "cyan" ]]; then
  echo -ne "\033[36m"
fi

while REPLY=; read -t 0.0$((1000/f)) -n 1 2>/dev/null; [[ -z $REPLY  ]]; do
  for (( i=1; i<=w; i++ )); do
    if [[ $NOLENGTH == 0 ]]; then
      if [[ ${y[i]} -gt 0 ]]; then
        tput cup ${y[i]} ${x[i]}
        echo -n " "
      fi
      ((y[i]+=v[i]))
      if [[ ${y[i]} -gt $h ]]; then
        ((y[i]=y[i]-h))
        ((x[i]=RANDOM*w/32768))
      fi
      if [[ ${y[i]} -gt 0 ]]; then
        tput cup ${y[i]} ${x[i]}
        echo -n "${sets[1]:1}"
      fi
    elif [[ $NOLENGTH == 1 ]]; then
      ((step=y[i]+v[i]))
      while [[ ${y[i]} -lt $step ]]; do
        if [[ ${y[i]} -gt 0 ]] && [[ ${y[i]} -lt $h ]]; then
          tput cup ${y[i]} ${x[i]}
          echo -n "${sets[1]:1}"
        fi
        ((y[i]+=1))
      done
      if [[ ${y[i]} -gt $h ]]; then
        ((y[i]=y[i]-h))
      fi
      ((step=e[i]+v[i]))
      while [[ ${e[i]} -lt $step ]]; do
        if [[ ${e[i]} -gt 0 ]] && [[ ${e[i]} -lt $h ]]; then
          tput cup ${e[i]} ${x[i]}
          echo -n " "
        fi
        ((e[i]+=1))
      done
      if [[ ${e[i]} -gt $h ]]; then
        ((e[i]=e[i]-h))
      fi
    fi
  done
done

cleanup
