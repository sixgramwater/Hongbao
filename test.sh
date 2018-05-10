#!/bin/bash

count=10
while [ $count -ge 0 ]
do
	echo $count;
	count=`expr $count - 1`
done

# Monitor a certain user to see if he is online now
until who | grep "$1" >/dev/null 2>&1
do 
	sleep 30
done
echo "be careful ! $1 is online now!"