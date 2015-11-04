from aloha import aloha
from graphics import giveMeTheGraphic
from matplotlib.pyplot import show

def lowerBound(x):
	return x*2

print "Rodando aloha..."
results = aloha(lowerBound)

emptySlots = []
colli = []
totalSlots = []
for i in results:
	emptySlots.append(i.numEmpty)
	colli.append(i.numCollision)
	totalSlots.append(i.numCollision + i.numIteration + i.numEmpty)

for result in results:
    print (result)

giveMeTheGraphic([(x+1)*100 for x in range(10)], emptySlots, "Iteracoes", "Slots Vazios")
giveMeTheGraphic([(x+1)*100 for x in range(10)], colli, "Iteracoes", "Colisoes")
giveMeTheGraphic([(x+1)*100 for x in range(10)], totalSlots, "Iteracoes", "Total de Slots")

show()
print "acabou"