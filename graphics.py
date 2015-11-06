import matplotlib.pyplot as plt
##import aloha

def _plotingresults(listx, listy, marc , subx, suby, index):
	plt.figure(index)
	plt.plot(listx, listy, marc)
	plt.ylabel(suby)
	plt.xlabel(subx)

# numero de tags, pelo numero de colisoes,  r = cor da linha -- = pontinhada
# _plotingresults((1,2,3,4), (1,2,4,5), 'r--', 'Alguns Numeros' , 'OUTROS NUMEROS')

def giveMeTheGraphic(listX, listY, subX, subY, index):	
	_plotingresults(listX, listY, 'o-', subX, subY, index)