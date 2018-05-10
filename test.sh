#!/bin/bash

count=10
while [ $count -ge 0 ]
do
	echo $count;
	count=`expr $count - 1`
done
