
#c, A_ub, b_ub, A_eq, b_eq
# x_p, y_p, x1, y1, dx1, dy1, d1,   x2, y2, dx2, dy2, d2 itd...   (wektor c)
class przygotowanieDanych:
    def __init__(self, iloscKlientow,dane):
        self.iloscKlientow = iloscKlientow 
        self.c = [0 for i in range(iloscKlientow*5+2)] #[0]*(iloscKlientow*5+2)
        self.A_ub = [[0 for i in range(iloscKlientow*5+2)] for j in range(iloscKlientow*5)]  #[[0]*(iloscKlientow*5+2)]*iloscKlientow*5
        self.b_ub = [0 for i in range(iloscKlientow*5)]  #[0]*iloscKlientow*5  
        self.A_eq = [[0 for i in range(iloscKlientow*5+2)] for j in range(iloscKlientow*2)] #[[0]*(iloscKlientow*5+2)]*iloscKlientow*2
        self.b_eq = [0 for i in range(iloscKlientow*2)]  #[0]*iloscKlientow*2
        self.macierzParametrowDoOptymalizacji()
        self.macierzOgraniczen()
        #self.wektorZerowy()
        self.macierzWspolrzednychKlientow()
        self.wektorWspolrzendnychKlientow(dane)

    #c
    def macierzParametrowDoOptymalizacji(self):
        for i in range(6,len(self.c),5):
            self.c[i]=1


    #A_ub
    def macierzOgraniczen(self):
        for i in range(self.iloscKlientow):  #kazdy wprowadza 5 ograniczen
            self.A_ub[0+i*5][4+i*5]=1
            self.A_ub[0+i*5][5+i*5]=1
            self.A_ub[0+i*5][6+i*5]=-1

            self.A_ub[1+i*5][0]=1  #wsp niezmienna
            self.A_ub[1+i*5][2+i*5]=-1
            self.A_ub[1+i*5][4+i*5]=-1

            self.A_ub[2+i*5][0]=-1 #wsp niezmienna
            self.A_ub[2+i*5][2+i*5]=1
            self.A_ub[2+i*5][4+i*5]=-1

            self.A_ub[3+i*5][1]=1 #wsp niezmienna
            self.A_ub[3+i*5][3+i*5]=-1
            self.A_ub[3+i*5][5+i*5]=-1

            self.A_ub[4+i*5][1]=-1 #wsp niezmienna
            self.A_ub[4+i*5][3+i*5]=1
            self.A_ub[4+i*5][5+i*5]=-1

    #A_eq
    def macierzWspolrzednychKlientow(self):
        for i in range(self.iloscKlientow):
            #print(i*2,2+i*5)
            self.A_eq[i*2][2+i*5]=1
            self.A_eq[1+i*2][3+i*5]=1

            #self.A_eq[i*2][3+i*5]=1
            #self.A_eq[1+i*2][2+i*5]=1

    #b_eq
    def wektorWspolrzendnychKlientow(self,dane):
        index=0
        for i in dane:
            for k in i:
                self.b_eq[index]=k
                index+=1