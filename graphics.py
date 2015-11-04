import matplotlib.pyplot as plt
##import aloha
index = 1

def _plotingresults(listx, listy, marc , subx, suby):
	plt.figure(index)
	plt.plot(listx, listy, marc)
	plt.ylabel(suby)
	plt.xlabel(subx)
	global index
	index += 1

# numero de tags, pelo numero de colisoes,  r = cor da linha -- = pontinhada
# _plotingresults((1,2,3,4), (1,2,4,5), 'r--', 'Alguns Numeros' , 'OUTROS NUMEROS')

def giveMeTheGraphic(listX, listY, subX, subY):	
	_plotingresults(listX, listY, 'o-', subX, subY)