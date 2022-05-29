# Python program for the above approach
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
PI = 3.141592653589

#współrzędne Wrocławia w stopniach punkt najbardziej na lewo i w dół
wsp=[51+(0.043413/0.6), 16+(0.552628/0.6)]
# ile punktów chcemy wygenerować
N = int(input("Ile punktów wygenerować: "))
fileName = input("Podaj nazwę pliku w którym zostaną zapisane wygenerowane dane (bez rozszerzenia):\n")


#generowanie punktów na prostokącie
# do punktu o najmniejszych współrzędnych x i y dodajemy długości tak aby utworzyć prostokąt
# odpowiednio promien_y i promien_x przemnożony przed random z przedzialu (0,1)
def randPoint(n):
    res = list()
    promien_y=(51.085497 - 51.043413)/0.6
    promien_x=(17.064902-17+16.6-16.552628)/0.6
    for i in range(n):
        res.append([
            round(wsp[0]+random.random()*promien_y*0.99, 5),
			round(wsp[1]+random.random()*promien_x*0.99, 5)
			 ])
 
    # Return the N points
    return res

# Wywołanie funkcji 
lista = randPoint(N)

# zapisywanie do pliku csv
header = ['lat', 'lng']
with open('../data/'+fileName+'.csv', 'w', encoding='UTF8', newline='') as f:
	writer = csv.writer(f, delimiter = ";")
	writer.writerow(header)

	#zapisywanie pozycji
	for pos in lista:
		# przygotowanie plota dla zobrazowania
		plt.scatter(x=pos[0], y=pos[1])
		writer.writerow(pos)

# wyświetlanie plota
#plt.gca().set_aspect('equal')
plt.show()

