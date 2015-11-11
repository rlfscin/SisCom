import os, random

def generator():
    
    if not os.path.exists("data128"):
            os.makedirs("data128")
    for numTags in [(x+1)*100 for x in range(10)]:
        lblFolder = "data/"+str(numTags)
        if not os.path.exists(lblFolder):
            os.makedirs(lblFolder)
        for lblFile in range(1000):
            addedTags = []
            tags = numTags
            while(tags != 0):
                tag = createTag()
                if not tag in addedTags:
                    addedTags.append(tag)
                    tags = tags - 1
            f = open(lblFolder + '/'+ str(lblFile+1) +'.txt' , 'w')
            for tag in addedTags:
                f.write(tag+"\n")
            f.close()
        
def createTag():
    rand = lambda: random.choice(['0','1']) 
    tagSize = 128
    tag = ''
    for i in range(tagSize):
        tag = tag + rand()
    return tag
    
generator()
