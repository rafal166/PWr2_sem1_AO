from scipy.cluster.vq import vq, kmeans
import csv
import matplotlib.pyplot as plt
from programowanieLiniowe import *
from scipy.optimize import linprog

p = int(input("Liczba paczkomatow: "))  # liczba paczkomatow
kolory=["red","green","blue","yellow","orange","purple","beige","brown","gray","cyan","magenta"] 
dane_stopnie=list()
dane_km=list()
stopien_pion=184*0.6   #w duzym zaokragleniu
stopien_poziom=116*0.6 #w duzym zaokragleniu
wsp=[51+(0.043413/0.6), 16+(0.552628/0.6)]
promien_y=(51.085497 - 51.043413)/0.6
promien_x=(17.064902-17+16.6-16.552628)/0.6
wsp_y=[wsp[0],wsp[0]+promien_y]
wsp_x=[wsp[1],wsp[1]+promien_x]
mapa = plt.imread("geoMapa_.png")

#jest rozdzielenie pomiędzy danymi wyrażonymi w stopniach a tych w km, dlaczego?
#dlatego, iż stopień w pionie nie jest równy (km) stopniowi w poziomie i dlatego podanie 
#danych w taki sposób do algorytmu skutkowało jego nieprawidłowym działaniem, 
#dlatego szacowałem z mapki z geoportalu długości które odpowiadają 1 stopniowi dla pionu i poziomu 
# i powiedzmy że to odpowiednio przeliczyłem, na mapie wygląda dobrze.


#funkcja do plotowania wszystkiegom podajemy:
# klaster - lista list, mamy tutaj liste, która zawiera listy, które zawierają punkty, analogicznie
# lista 1 to 1 klaster itd...
# wsp_paczkomatu to lista kolejnych współrzędne paczkomatów
def plot_mapa(klaster,wsp_paczkomatu):
    mapa = plt.imread("geoMapa_.png")
    plt.imshow(mapa)
    plt.yticks([0,int(mapa.shape[0]/2),mapa.shape[0]-1],[round(wsp_y[1],4),round(wsp_y[0]+(wsp_y[1]-wsp_y[0])/2,4),round(wsp_y[0],4)])
    plt.xticks([0,int(mapa.shape[1]/2),mapa.shape[1]-1],[round(wsp_x[0],4),round(wsp_x[0]+(wsp_x[1]-wsp_x[0])/2,4),round(wsp_x[1],4)])
    #print(mapa.shape)
    for i,klaster_ in enumerate(klaster):
        for pkt in klaster_:
            plt.scatter(y=((pkt[0]-wsp_y[0])/(wsp_y[1]-wsp_y[0])*mapa.shape[0]),x=((pkt[1]-wsp_x[0])/(wsp_x[1]-wsp_x[0])*mapa.shape[1]),color =kolory[i%len(kolory)])
        plt.scatter(y=((wsp_paczkomatu[i][0]-wsp_y[0])/(wsp_y[1]-wsp_y[0])*mapa.shape[0]),x=((wsp_paczkomatu[i][1]-wsp_x[0])/(wsp_x[1]-wsp_x[0])*mapa.shape[1]),color ="black")
    #plt.gca().set_aspect('equal')
    plt.show()


fileName = input("Podaj nazwe pliku w ktorym sa dane (bez rozszerzenia):\n")

with open('data/'+fileName+'.csv') as f:
    csv_reader = csv.reader(f, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
        else:
            dane_stopnie.append([float(row[0]), float(row[1])]) #wczytanie danych do listy, która zawiera dane w stopniach
            dane_km.append([(float(row[0])-wsp[0])*stopien_pion, (float(row[1])-wsp[1])*stopien_poziom]) #wczytanie danych do listy, która zawiera dane w km
        line_count+=1

wspolrzedneSrodkaKlastra, promienKlastra = kmeans(dane_km, p) #algorytm k średnich, rozdzielenie danych na mniejsze podproblemy
indexKlastra, _ = vq(dane_km, wspolrzedneSrodkaKlastra) #indexKlastra to lista, która mówi po kolei który punkt do którego klastra należy

#pogrupowanie danych 
klastry_km = [[] for i in range(p)]
klastry_stopnie = [[] for i in range(p)]
for i in range(len(indexKlastra)):
    klastry_km[indexKlastra[i]].append(dane_km[i])
    klastry_stopnie[indexKlastra[i]].append(dane_stopnie[i])


wsp_paczkomatow = [[] for i in range(p)]
wsp_paczkomatow_km = [[] for i in range(p)]
#test=przygotowanieDanych(len(klastry_km[0]),klastry_km[0])

#no i zastosowanie algorytmu
for i in range(p):
    test=przygotowanieDanych(len(klastry_km[i]),klastry_km[i])
    res = linprog(test.c, A_ub=test.A_ub, b_ub=test.b_ub, A_eq=test.A_eq, b_eq=test.b_eq, method = 'simplex')
    wsp_paczkomatow[i].append(res.x[0]/stopien_pion+wsp[0]) 
    wsp_paczkomatow[i].append(res.x[1]/stopien_poziom+wsp[1])
    wsp_paczkomatow_km[i].append(res.x[0]) 
    wsp_paczkomatow_km[i].append(res.x[1])
    #print("Wspolrzedne paczkomatu",str(i),": ",wsp_paczkomatow[i][0],wsp_paczkomatow[i][1])
    #print("Wspolrzedne paczkomatu",str(i),": ",res.x[0],res.x[1])

odleglosci_od_paczkomatu=[[] for i in range(p)]
for count,i in enumerate(klastry_km):
    for k in i:
        odleglosci_od_paczkomatu[count].append([abs(k[0]-wsp_paczkomatow_km[count][0])+abs(k[1]-wsp_paczkomatow_km[count][1])])

maksymalne_odleglosci=[]
for i in range(p):
    maksymalne_odleglosci.append(max(odleglosci_od_paczkomatu[i])[0])
    print("Wspolrzedne paczkomatu",str(i),": ",wsp_paczkomatow[i][0],wsp_paczkomatow[i][1]," Odleglosc najdalszego klienta: ",max(odleglosci_od_paczkomatu[i])[0],"km")
print("Odleglosc najbardziej oddalonego klienta ze wszystkich regionow od paczkomatu wynosi: ",max(maksymalne_odleglosci),"km")
plot_mapa(klastry_stopnie,wsp_paczkomatow)