class Result:
    def __init__(self, numIteration):
        self.numIteration = numIteration
        self.numEmpty = 0
        self.numCollision = 0
    def __str__(self):
        return "Number of iteration: " + str(self.numIteration) + '\n' +"Number of empty slots: " + str(self.numEmpty) + '\n' +"Number of collision: " + str(self.numCollision) + '\n' + "Numero total de slots: " + str(self.numIteration + self.numEmpty + self.numCollision) + '\n' 
    def add(self, r):
    	self.numEmpty = self.numEmpty + r.numEmpty
    	self.numCollision = self.numCollision + r.numCollision
    def __add__(self, r):
    	result = Result(self.numIteration)
    	result.numEmpty = self.numEmpty + r.numEmpty
    	result.numCollision = self.numCollision + r.numCollision
    	return result
    def __div__(self, k):
    	result = Result(self.numIteration)
    	result.numEmpty = 1.0*self.numEmpty/k
    	result.numCollision = 1.0*self.numCollision/k
    	return result