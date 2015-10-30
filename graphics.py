

import matplotlib.pyplot as plt
##import aloha


def _plotingresults(listx, listy, marc , subx, suby):
	plt.plot(listx, listy, marc)
	plt.ylabel(suby)
	plt.xlabel(subx)
	plt.show()

# numero de tags, pelo numero de colisões,  r = cor da linha -- = pontinhada 
_plotingresults((1,2,3,4), (1,2,4,5), 'r--', 'Alguns Numeros' , 'OUTROS NUMEROS')