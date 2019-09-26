#!bin/bash

res=$(find . -type f | wc -l)
echo "Total number of files:" $res
direc=$(find . -mindepth 1 -type d)
for name in $direc
do
	echo "Files in" $name ":" $(find $name -mindepth 1 -type f | wc -l)
done
currentdate=$(date +"%D %T")
previousdate=$(date --date="2 days ago")
#echo $currentdate
#touch --date previousdate /tmp/start
#touch --date currentdate /tmp/end
res1=$(find . -type f -newermt "$previousdate" ! -newermt "$currentdate" | wc -l)
#res=$(find . -type f -ls |grep '' |wc -l)
echo "No. of modified files: " $res1
#echo $res1
