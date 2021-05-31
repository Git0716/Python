#! /bin/bash

threshold="1"

mdir='/home'
echo $mdir
MAILTO='chusworld@yahoo.com'
SUBJECT="$mdir disk usage"

cd "$mdir"
for user in * ;do
  size=$(du -s $mdir | awk '{print $1}')
  if [[ $size -ge $threshold ]] 
   then
    
    echo $(du -sh $user | mailx -s $SUBJECT $MAILTO)
  fi
done
 
