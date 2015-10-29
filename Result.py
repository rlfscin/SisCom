class Result:
    def __init__(self, numInteration):
        self.numInteration = numInteration
        self.numEmpty = 0
        self.numCollision = 0
        self.time = 0
    def __str__(self):
        return "Number of interation: " + str(self.numInteration) + '\n' +"Number of empty slots: " + str(self.numEmpty) + '\n' +"Number of collision: " + str(self.numCollision) + '\n' + "Numero total de slots: " + str(self.numInteration + self.numEmpty + self.numCollision) + '\n' + "Time: " + str(self.time) + '\n' 
    def __add__(self, r):
    	result = Result(self.numInteration)
    	result.numEmpty = self.numEmpty + r.numEmpty
    	result.numCollision = self.numCollision + r.numCollision
    	result.time = self.time + r.time
    	return result
    def __div__(self, k):
    	result = Result(self.numInteration)
    	result.numEmpty = self.numEmpty/k
    	result.numCollision = self.numCollision/k
    	result.time = self.time/k
    	return result

r1 = Result(100)
r1.numEmpty = 10
r1.numCollision = 20
print r1

r2 = Result(100)
r2.numEmpty = 30
r2.numCollision = 40
print r2

r3 = r1 + r2

print r3

r4 = r3/2.0

print r4