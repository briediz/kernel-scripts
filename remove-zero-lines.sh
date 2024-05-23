#!/bin/bash
filename=$1
if [ $filename == "" ]; then
       echo "input file missing"
       exit
fi

n=1
while read line; do
if [[ $line == *"="* ]] || [[ $line == *"is not"* ]]
then
        echo "$line"
        n=$((n+1))
fi
done < $filename
