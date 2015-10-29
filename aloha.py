from Result import Result
from random import randint

def aloha(func):
    rand = lambda x: randint(0,x)
    results = []
    for numTags in [(x+1)*100 for x in range(10)]:
        numSlots = 64
        result = Result(numTags)
        while(numTags != 0):
            slots = [0]*numSlots
            numCollision = 0
            for tag in range(numTags):
                slot = rand(numSlots-1)
                slots[slot] = slots[slot] + 1
            for slot in slots:
                if(slot == 0):
                    result.numEmpty = result.numEmpty + 1;
                elif(slot == 1):
                    numTags = numTags - 1;
                else:
                    numCollision = numCollision + 1
            result.numCollision = result.numCollision + numCollision
            numSlots = func(numCollision)
        results.append(result)
    return results

def lowerBound(x):
    return x*2

def volt(x):
    return x

results = aloha(lowerBound)
results = aloha(volt)

for result in results:
    print (result.toString())
