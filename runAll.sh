#!/bin/bash

flex scanner.lex && g++ -std=c++17 lex.yy.c hw1.cpp -o hw1.out

for i in {1..28}
do
   ./hw1.out < td${i}.in > new_out.txt
   
   DIFF=$(diff td${i}.out new_out.txt)
    
    if [ "$DIFF" == "" ] 
    then
        echo "-- Test $i passed :D --"
    else
        echo "-- Test $i FAILED :'( --"
    fi
done



for i in {1..30}
do
   timeout 20s ./prfWorking $(echo ${params[$i]}) "program$i.out" \
			 > newstudout.txt

#     DIFF=$(diff out${i}_new.txt newstudout.txt)
    
#     if [ "$DIFF" == "" ] 
#     then
#         echo "-- Test $i passed :D --"
#     else
#         echo "-- Test $i FAILED :'( --"
#     fi
    
# done
