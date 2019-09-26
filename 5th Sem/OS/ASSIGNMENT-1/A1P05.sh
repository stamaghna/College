#!/bin/bash
read -p "Enter the file name: " file
read -p "Enter the string to search: " str
num=$(grep -c "$str" $file)
if [ $num -eq 0 ]; then
    echo "string not found"
    exit
fi
echo "number of occurances: $num"
echo -e "\nLine\tfreq"
linec=$(grep -o -n $str $file | cut -d : -f 1 | uniq -c | wc -l)
if [ $linec -eq 0 ]; then
    echo "String not found"
    exit 0
fi
echo "   Count Line"
grep -o -n $str $file | cut -d : -f 1 | uniq -c
