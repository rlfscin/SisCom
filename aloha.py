from Result import Result
from random import randint

def aloha(func):
    rand = lambda x: randint(0,x)
    results = []
    for numTags in [(x+1)*100 for x in range(10)]:
    	resultTotal = Result(numTags)
    	for i in range(1000):
	        numSlots = 64
	        result = Result(numTags)
	        numTagsCount = numTags
	        while(numTagsCount != 0):
	            slots = [0]*numSlots
	            numCollision = 0
	            for tag in range(numTagsCount):
	                slot = rand(numSlots-1)
	                slots[slot] = slots[slot] + 1
	            for slot in slots:
	                if(slot == 0):
	                    result.numEmpty = result.numEmpty + 1;
	                elif(slot == 1):
	                    numTagsCount = numTagsCount - 1;
	                else:
	                    numCollision = numCollision + 1
	            result.numCollision = result.numCollision + numCollision
	            numSlots = func(numCollision)
	        resultTotal.add(result)
        results.append(resultTotal/1000)
    return results

def lowerBound(x):
    return x*2

def eomLee(x):
    return x*2 #TODO

results = aloha(lowerBound)
#results = aloha(eomLee)

for result in results:
    print (result)
