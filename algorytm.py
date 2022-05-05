from scipy.cluster.vq import vq, kmeans
import csv
import matplotlib.pyplot as plt

p=10  # liczba paczkomatow
kolory=["red","green","blue","yellow","black","orange","purple","beige","brown","gray","cyan","magenta"]
dane_stopnie=list()
dane_km=list()
stopien_pion=1.84   #w duzym zaokragleniu
stopien_poziom=1.16 #w duzym zaokragleniu
wsp=[51+(0.043413/0.6), 16+(0.552628/0.6)]
promien_y=(51.085497 - 51.043413)/0.6
promien_x=(17.064902-17+16.6-16.552628)/0.6
wsp_y=[wsp[0],wsp[0]+promien_y]
wsp_x=[wsp[1],wsp[1]+promien_x]

def plot_mapa(dane,indexKlastra):
    mapa = plt.imread("geoMapa_.png")
    plt.imshow(mapa)
    plt.yticks([0,int(mapa.shape[0]/2),mapa.shape[0]-1],[round(wsp_y[1],4),round(wsp_y[0]+(wsp_y[1]-wsp_y[0])/2,4),round(wsp_y[0],4)])
    plt.xticks([0,int(mapa.shape[1]/2),mapa.shape[1]-1],[round(wsp_x[0],4),round(wsp_x[0]+(wsp_x[1]-wsp_x[0])/2,4),round(wsp_x[1],4)])
    #print(mapa.shape)
    for i,pkt in enumerate(dane):
        plt.scatter(y=((pkt[0]-wsp_y[0])/(wsp_y[1]-wsp_y[0])*mapa.shape[0]),x=((pkt[1]-wsp_x[0])/(wsp_x[1]-wsp_x[0])*mapa.shape[1]),color =kolory[indexKlastra[i]])
    #plt.gca().set_aspect('equal')
    plt.show()


fileName = input("Podaj nazwę pliku w którym są dane:\n")

with open('data/'+fileName+'.csv') as f:
    csv_reader = csv.reader(f, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
        else:
            dane_stopnie.append([float(row[0]), float(row[1])])
            dane_km.append([(float(row[0])-wsp[0])*stopien_pion, (float(row[1])-wsp[1])*stopien_poziom])
        line_count+=1

wspolrzedneSrodkaKlastra, promienKlastra = kmeans(dane_km, p)
indexKlastra, _ = vq(dane_km, wspolrzedneSrodkaKlastra)

plot_mapa(dane_stopnie,indexKlastra)