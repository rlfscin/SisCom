from aloha import *
from graphics import giveMeTheGraphic
from matplotlib.pyplot import show

print "Rodando Lower Bound..."
resultsLB = aloha(lowerBound)
print "Agora rodando o EomLee..."
resultsEL = aloha(eomLee)
print "Agora rodando o Chen..."
resultsCH = aloha(chen)

emptySlots = []
colli = []
totalSlots = []

emptySlots2 = []
colli2 = []
totalSlots2 = []

emptySlots3 = []
colli3 = []
totalSlots3 = []

for i in resultsLB:
	emptySlots.append(i.numEmpty)
	colli.append(i.numCollision)
	totalSlots.append(i.numCollision + i.numIteration + i.numEmpty)

for j in resultsEL:
	emptySlots2.append(j.numEmpty)
	colli2.append(j.numCollision)
	totalSlots2.append(j.numCollision + j.numIteration + j.numEmpty)

for k in resultsCH:
	emptySlots3.append(k.numEmpty)
	colli3.append(k.numCollision)
	totalSlots3.append(k.numCollision + k.numIteration + k.numEmpty)

for rlb in resultsLB:
    print (rlb)
for rel in resultsEL:
    print (rel)
for rch in resultsCH:
    print (rch)

giveMeTheGraphic([(x+1)*100 for x in range(10)], emptySlots, "Iteracoes", "Slots Vazios", 1)
giveMeTheGraphic([(x+1)*100 for x in range(10)], emptySlots2, "Iteracoes", "Slots Vazios", 1)
giveMeTheGraphic([(x+1)*100 for x in range(10)], emptySlots3, "Iteracoes", "Slots Vazios", 1)
giveMeTheGraphic([(x+1)*100 for x in range(10)], colli, "Iteracoes", "Colisoes", 2)
giveMeTheGraphic([(x+1)*100 for x in range(10)], colli2, "Iteracoes", "Colisoes", 2)
giveMeTheGraphic([(x+1)*100 for x in range(10)], colli3, "Iteracoes", "Colisoes", 2)
giveMeTheGraphic([(x+1)*100 for x in range(10)], totalSlots, "Iteracoes", "Total de Slots", 3)
giveMeTheGraphic([(x+1)*100 for x in range(10)], totalSlots2, "Iteracoes", "Total de Slots", 3)
giveMeTheGraphic([(x+1)*100 for x in range(10)], totalSlots3, "Iteracoes", "Total de Slots", 3)

show()
print "Acabou."
