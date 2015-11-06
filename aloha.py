from Result import Result
from random import randint
from math import exp

from scipy.misc import factorial

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
	            numEmpty = 0
	            numSuccess = 0
	            for tag in range(numTagsCount):
	                slot = rand(numSlots-1)
	                slots[slot] = slots[slot] + 1
	            for slot in slots:
	                if(slot == 0):
	                	numEmpty = numEmpty + 1
	                elif(slot == 1):
	                	numSuccess = numSuccess + 1
	                else:
	                    numCollision = numCollision + 1
	            result.numCollision = result.numCollision + numCollision
	            result.numEmpty = result.numEmpty + numEmpty;
	            numTagsCount = numTagsCount - numSuccess;
	            
	            total = numCollision + numSuccess + numEmpty
	            
	            numSlots = func({'collision' : numCollision, 'empty' : numEmpty, 'success' : numSuccess})
	        resultTotal.add(result)
        results.append(resultTotal/1000)
    return results


def lowerBound(result):
    return result['collision']*2

def eomLee(result):
    b = float('inf')
    y = 2.0
    t = 0.001
    l = result['collision'] + result['success'] + result['empty']
    while True:
    	b = l/(result['collision']*y + result['success'])
    	ny = (1 - exp( -1 / b)) / (b*(1 - (1 + 1/b)*exp(-1/b)))
    	if(abs(y - ny) < t):
    		break
    	y = ny
    
    f = y * result['collision']
    
    return int(y * result['collision'])

def chen(result):
    l = result['empty'] + result['success'] + result['collision']
    n = result['success'] + 2 * result['collision']
    next = 0
    previous = -1
    while previous < next:
        pe = (1.0 - (1.0/l)) ** n
        ps = (n/l) * ((1.0 - (1.0/l)) ** (n - 1))
        pc = 1.0 - pe - ps
        previous = next
        next = (factorial(l) / (factorial(result['empty']) * factorial(result['success']) * factorial(result['collision']))) * (pe ** result['empty']) * (ps ** result['success']) * (pc ** result['collision'])
        n += 1
    return n - 2
