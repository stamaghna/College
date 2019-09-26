#!/bin/bash

read -p "Enter file name 1: " f1
read -p "Enter file name 2: " f2
read -p "Enter file name 3: " f3
read -p "Enter file name 4: " f4
printf1=$(grep -wc "printf" $f1)
scanf1=$(grep -wc "scanf" $f1)
int1=$(grep -wc "int" $f1)
printf2=$(grep -wc "printf" $f2)
scanf2=$(grep -wc "scanf" $f2)
int2=$(grep -wc "int" $f2)
printf3=$(grep -wc "printf" $f3)
scanf3=$(grep -wc "scanf" $f3)
int3=$(grep -wc "int" $f3)
printf4=$(grep -wc "printf" $f4)
scanf4=$(grep -wc "scanf" $f4)
int4=$(grep -wc "int" $f4)
echo -e "File \t\t printf \t\t scanf \t\t int"
echo -e "$f1 \t $printf1 \t\t $scanf1 \t $int1"
echo -e "$f2 \t $printf2 \t\t $scanf2 \t $int2"
echo -e "$f3 \t $printf3 \t\t $scanf3 \t $int3"
echo -e "$f4 \t $printf4 \t\t $scanf4 \t $int4"