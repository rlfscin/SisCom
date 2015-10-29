class Result:
    def __init__(self, numInteration):
        self.numInteration = numInteration
        self.numEmpty = 0
        self.numCollision = 0
        self.time = 0
    def toString(self):
        return "Number of interation: " + str(self.numInteration) + '\n' +"Number of empty slots: " + str(self.numEmpty) + '\n' +"Number of collision: " + str(self.numCollision) + '\n' + "Numero total de slots: " + str(self.numInteration + self.numEmpty + self.numCollision) + '\n' + "Time: " + str(self.time) + '\n' 
