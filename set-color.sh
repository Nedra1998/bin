COLOR="$1"
if [ "$COLOR" == "Default" ]
then
  printf "\e[0m"
else
  printf "\e[38;5;"$COLOR"m"
fi
