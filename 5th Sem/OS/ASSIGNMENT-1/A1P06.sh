#!/bin/bash

read -p "Enter the file name: " file
read -p "Enter the string to search: " str
num=0
fullmatches=0
partialmathches=0
num=$(grep -c "$str" $file)
fullmatches=$(grep -wc "$str" $file)
partialmatches=$(($num - $fullmatches))

if [ $num -eq 0 ]; then
    echo "string not found"
    exit 0
else
    echo "number of occurances: $num"
    if (($fullmatches==0)); then
        echo "number of whole matches: 0"
    else
        echo "number of whole matches: $fullmatches"
    fi
    if (($partialmatches==0)); then
        echo "number of partial matches: 0"
    else
        echo "number of partial matches: $partialmatches"
    fi
fi
if (($fullmatches!=0)); then
    read -p "Enter the string to replace with: " new
    sed -i "s/\b$str\b/$new/g" $file
fi