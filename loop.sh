#!/bin/bash 

# script that prints the first two argument with 2.5 seconds of gap.

for n in {1..5}
do
   echo $n
   sleep .5
done
echo $1

for n in {1..5}
do
   echo $n
   sleep .5
done
echo $2