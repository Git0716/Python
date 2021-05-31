#! /bin/bash

STRING="Null Byte"
echo "Hackers love to learn on $STRING"
echo "I firmly believe tht $1 is the best $2 for the office of $3"
alias myrequest= echo "$(w |grep ec2 | awk '{print $1 $3}')"
echo "here is my info $myrequest"
echo "what is your name?"
read name
set -x
if [ "$name" ]
 then
  echo "$name sounds alright"
else
   echo "$name sound like nothing to me"
echo " wow $name is crazy"
fi

set +x
