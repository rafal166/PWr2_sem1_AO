# Python program for the above approach
import math
import random
import numpy as np
import matplotlib.pyplot as plt
import csv
PI = 3.141592653589;

#współrzędne Wrocławia
wLat = 51.1079
wLng = 17.0385
promienWroclawia = 0.8 # zakładam, że taki okrąg to Wrocław
# ile punktów chcemy wygenerować
N = int(input("Ile punktów wygenerować: "))
fileName = input("Podaj nazwę pliku w którym zostaną zapisane wygenerowane dane (bez rozszerzenia):\n")

def randPoint2(r, x, y, n):
    res = list();
    wsp=[51+(0.043413/0.6), 16+(0.552628/0.6)]
    promien_y=(51.085497 - 51.043413)/0.6
    promien_x=(17.064902-17+16.6-16.552628)/0.6
    for i in range(n):
        res.append([
            round(wsp[0]+random.random()*promien_y*0.99, 5),
			round(wsp[1]+random.random()*promien_x*0.99, 5)
			 ]);
 
    # Return the N points
    return res;

def randPoint(r, x, y, n):
    res = list();
 
    for i in range(n):
        # Get Angle in radians
        theta = 2 * PI * random.random();
        # Get length from center
        len = math.sqrt(random.random()) * r;
        # Add point to results.
        res.append([
			round(x + len * math.cos(theta), 5),
			round(y + len * math.sin(theta), 5)
			 ]);
 
    # Return the N points
    return res;

# Wywołanie funkcji 
lista = randPoint2(promienWroclawia, wLat, wLng, N)

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

