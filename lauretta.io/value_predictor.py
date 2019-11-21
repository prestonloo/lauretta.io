#!/usr/bin/env python

'''
Task 1:
Create in a github repo for this test
Have a file value_predictor.py or equivalent that takes a list of an even number of value and is of at minimum length of 6 sequential and increasing elements and find the most likely middle value.
Test case:
value_predictor([1,2,3,4,5,6]) should return 3.5
value_predictor([1,1,1,6,6,6]) should return either 3.5 closer to 3.45 depending on method
'''

def value_predictor(inputList):
    
    #get the middle indexes of the list
    middleValue1 = len(inputList) / 2 - 1
    middleValue2 = len(inputList) / 2
    
    #convert the middle indexes from float to integer
    middleValue1 = int(middleValue1)
    middleValue2 = int(middleValue2)
    
    #computer most likely middlevalue
    result = (inputList[middleValue1] + inputList[middleValue2]) / 2
    
    #display result
    print(result)
    
    
#below are the test cases
value_predictor([1,2,3,4,5,6])          #should return 3.5
value_predictor([1,1,1,6,6,6])          #should return 3.5
value_predictor([2,4,6,8,12,18])        #should return 7
value_predictor([2,4,6,8,12,20])        #should return 7
value_predictor([2,4,6,8,12,18,20,22])  #should return 10
