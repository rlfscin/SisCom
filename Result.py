class Result:
    def __init__(self, numInteration):
        self.numInteration = numInteration
        self.numEmpty = 0
        self.numCollision = 0
        self.time = 0
    def __str__(self):
        return "Number of interation: " + str(self.numInteration) + '\n' +"Number of empty slots: " + str(self.numEmpty) + '\n' +"Number of collision: " + str(self.numCollision) + '\n' + "Numero total de slots: " + str(self.numInteration + self.numEmpty + self.numCollision) + '\n' + "Time: " + str(self.time) + '\n' 
    def add(self, r):
    	self.numEmpty = self.numEmpty + r.numEmpty
    	self.numCollision = self.numCollision + r.numCollision
    	self.time = self.time + r.time
    def __add__(self, r):
    	result = Result(self.numInteration)
    	result.numEmpty = self.numEmpty + r.numEmpty
    	result.numCollision = self.numCollision + r.numCollision
    	result.time = self.time + r.time
    	return result
    def __div__(self, k):
    	result = Result(self.numInteration)
    	result.numEmpty = 1.0*self.numEmpty/k
    	result.numCollision = 1.0*self.numCollision/k
    	result.time = 1.0*self.time/k
    	return result