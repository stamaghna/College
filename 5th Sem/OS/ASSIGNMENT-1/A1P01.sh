#!/bin/sh

while(true)
do
	read -p "Input-1:" userv1
	read -p "Input-2:" userv2
	if [[ $userv1 == [a-zA-Z] ]]
	then
		userv1=0
	fi
	if [[ $userv2 == [a-zA-Z] ]]
	then
		userv2=0
	fi
	resadd=$(echo "scale=2;$userv1+$userv2" | bc)
	echo "Addition:" $resadd
	resmul=$(echo "scale=2;$userv1*$userv2" | bc)
	echo "Multiplication:" $resmul
	if [ $userv2 != 0 ]
	then
   		resdiv=$(echo "scale=2;$userv1/$userv2" | bc)
   		echo "Division:" $resdiv
   	else
   		echo "Error"
	fi
	read -p "Continue?Y/N:" confirm
	if [[ $confirm != [Yy] ]]
	then
		exit 0
	fi
done		
