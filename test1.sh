#! /bin/bash

while IFS="a" read -r LINE; do
  echo "$LINE" 

done < "$1"


