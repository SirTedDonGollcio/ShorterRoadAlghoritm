import turtle
import wierzcholek
import krawedz
import math
import kabel
 
 
class Graf():
    wierzcholkiR = []
    krawedzieR = []
    kableR = []
    iloscKrawedziR=0
    iloscWierzcholkowR=0
    iloscKabliR=0

    def odczyt(self):
        
        with open('network.txt') as plik:
            linie = []
            for linia in plik:
                if linia.strip().split()[0] != "#":
                    linie.append(linia)


            iloscWierzcholkow = int(linie[0][8:(len(linie[0])-1)])
        
            wierzcholki = []

            for i in range(1,iloscWierzcholkow+1):
                linie[i]=linie[i].strip().split()
                tempW = wierzcholek.Wierzcholek(int(linie[i][0]),int(linie[i][1]),int(linie[i][2]),int(linie[i][3]))
                wierzcholki.append(tempW)

            iloscKrawedzi = int(linie[iloscWierzcholkow+1][12:(len(linie[iloscWierzcholkow+1])-1)])

            krawedzie = []
            

            for i in range((iloscWierzcholkow+2),(iloscWierzcholkow+iloscKrawedzi+2)):
                linie[i]=linie[i].strip().split()
                tempK = krawedz.Krawedz(int(linie[i][0]),int(linie[i][1]),int(linie[i][2]))
                krawedzie.append(tempK)

            iloscKabli = int(linie[iloscKrawedzi+iloscWierzcholkow+2][8:(len(linie[iloscKrawedzi+iloscWierzcholkow+2])-1)])
            
            kable = []

            for i in range((iloscKrawedzi+iloscWierzcholkow+3),(iloscKabli+iloscWierzcholkow+iloscKrawedzi+3)):
                linie[i]=linie[i].strip().split()
                tempK = kabel.Kabel(int(linie[i][0]),int(linie[i][1]),int(linie[i][2]))
                kable.append(tempK)

          
            #jest juz lista z wczytaniymi wierzcholkami i krawedziami jako klasy i to jest "wierzcholki" i "krawedzie"

            for i in range(iloscKrawedzi):
                krawedzie[i].waga = round(math.sqrt(pow((wierzcholki[(krawedzie[i].koniec)-1].wspolrzedneX)-(wierzcholki[(krawedzie[i].poczatek)-1].wspolrzedneX),2) + pow((wierzcholki[(krawedzie[i].koniec)-1].wspolrzedneY)-(wierzcholki[(krawedzie[i].poczatek)-1].wspolrzedneY),2)))
                

            self.krawedzieR = krawedzie
            self.wierzcholkiR = wierzcholki
            self.kableR = kable
            self.iloscKrawedziR = iloscKrawedzi
            self.iloscWierzcholkowR = iloscWierzcholkow
            self.iloscKabliR = iloscKabli


          
  
    def rysuj(self):

        wspx = []
        wspy = []
        kraP = []
        kraK = []

        turtle.setworldcoordinates(0, 0, 100, 100)

        for i in range (0,self.iloscWierzcholkowR):
            wspx.insert(i, self.wierzcholkiR[i].wspolrzedneX)
            wspy.insert(i, self.wierzcholkiR[i].wspolrzedneY)

        for i in range (0,self.iloscKrawedziR):
            kraP.insert(i, self.krawedzieR[i].poczatek)
            kraK.insert(i, self.krawedzieR[i].koniec)

        #print(wspx,wspy,kraP,kraK)
        
        turtle.pensize(1)
        turtle.pencolor(0,0,0)
        for j in range (0,self.iloscKrawedziR):
            turtle.pu()
            turtle.goto(wspx[kraP[j]-1],wspy[kraP[j]-1])
            turtle.pd()
            turtle.goto(wspx[kraK[j]-1],wspy[kraK[j]-1])

    def prim(self):
        
        odwiedzone = []
        nieodwiedzone = self.wierzcholkiR[:]
        odwiedzone.append(self.wierzcholkiR[0])
        nieodwiedzone.remove(self.wierzcholkiR[0])
        przeszle = []
        doprzejscia = self.krawedzieR[:]
        

       
        while nieodwiedzone:
       
            najkrotszy=0
            aktualny=0

            for j in range(len(odwiedzone)):       
                for i in range(len(doprzejscia)):
                     bylo=0
                     if((doprzejscia[i].poczatek == odwiedzone[j].id)or(doprzejscia[i].koniec == odwiedzone[j].id)):
                         
                         for iterr in range(len(odwiedzone)):
                             if(doprzejscia[i].poczatek == odwiedzone[iterr].id):
                                 bylo+=1
                             elif(doprzejscia[i].koniec == odwiedzone[iterr].id):
                                 bylo+=1

                         if(bylo!=2):
                             if(najkrotszy==0):
                                 najkrotszy=doprzejscia[i].id
                                 if(doprzejscia[i].poczatek == odwiedzone[j].id):
                                    aktualny=odwiedzone[j].id
                                 else:
                                    aktualny=self.wierzcholkiR[doprzejscia[i].koniec-1].id

                             elif(self.krawedzieR[najkrotszy-1].waga>doprzejscia[i].waga):
                                 najkrotszy=doprzejscia[i].id
                                 if(doprzejscia[i].poczatek == odwiedzone[j].id):
                                    aktualny=odwiedzone[j].id
                                 else:
                                    aktualny=self.wierzcholkiR[doprzejscia[i].koniec-1].id

            #print("%",najkrotszy,aktualny,"%")

            if(self.wierzcholkiR[aktualny-1].id==self.krawedzieR[najkrotszy-1].poczatek):
                
                przeszle.append(self.krawedzieR[najkrotszy-1])
                odwiedzone.append(self.wierzcholkiR[self.krawedzieR[najkrotszy-1].koniec-1])
                nieodwiedzone.remove(self.wierzcholkiR[self.krawedzieR[najkrotszy-1].koniec-1])
                doprzejscia.remove(self.krawedzieR[najkrotszy-1])

            elif(self.wierzcholkiR[aktualny-1].id==self.krawedzieR[najkrotszy-1].koniec):
                
                przeszle.append(self.krawedzieR[najkrotszy-1])
                odwiedzone.append(self.wierzcholkiR[self.krawedzieR[najkrotszy-1].poczatek-1])
                nieodwiedzone.remove(self.wierzcholkiR[self.krawedzieR[najkrotszy-1].poczatek-1])
                doprzejscia.remove(self.krawedzieR[najkrotszy-1])

            #for i in range(len(odwiedzone)):
            #    print(odwiedzone[i].id)
            #print("-----")
            #
            #for i in range(len(nieodwiedzone)):
            #    print(nieodwiedzone[i].id)
            #print("-----")
            #
            #for i in range(len(przeszle)):
            #    print(przeszle[i].id," ",przeszle[i].poczatek," ",przeszle[i].koniec)
            #print("-----")
        
        #self.rysuj()

        wspx = []
        wspy = []
        kraP = []
        kraK = []

        for i in range (0,self.iloscWierzcholkowR):
            wspx.insert(i, self.wierzcholkiR[i].wspolrzedneX)
            wspy.insert(i, self.wierzcholkiR[i].wspolrzedneY)

        for i in range (0,len(przeszle)):
            kraP.insert(i, przeszle[i].poczatek)
            kraK.insert(i, przeszle[i].koniec)

        #print(wspx,wspy,kraP,kraK)
        
        turtle.pensize(5)
        turtle.pencolor('#FF0000')
        for j in range (0,len(przeszle)):
            turtle.pu()
            turtle.goto(wspx[kraP[j]-1],wspy[kraP[j]-1])
            turtle.pd()
            turtle.goto(wspx[kraK[j]-1],wspy[kraK[j]-1])


    def dijkstra(self,pocz,kon,mozliwosc):
        #pocz = int(input("Podaj początkowy wierzchołek(id)\n")) 
        #kon = int(input("Podaj końcowy wierzchołek(id)\n")) 

        if(pocz > self.iloscWierzcholkowR or kon > self.iloscWierzcholkowR):
            print("Zły wierzchołek")
            return
            
        
        zbadane = {}
        niezbadane = {}
        for i in range (1,self.iloscWierzcholkowR+1):
            niezbadane[i]=10000000
        

        kraNast = [-2 for _ in range (0,self.iloscWierzcholkowR)]
            
        niezbadane[pocz] = 0
        kraNast[pocz-1] = -1

        zbadane[pocz]=0
        for i in range (1,self.iloscWierzcholkowR+1):
                if (i not in zbadane.keys()):
                    for j in range (0,self.iloscKrawedziR):
                        if(self.krawedzieR[j].poczatek == i or self.krawedzieR[j].poczatek == pocz):
                            if(self.krawedzieR[j].koniec == i or self.krawedzieR[j].koniec == pocz):
                                kraNast[i-1] = self.wierzcholkiR[pocz-1].id
                                niezbadane[i] = self.krawedzieR[j].waga
    

        #print(niezbadane)
        del niezbadane[pocz]
        
        while niezbadane.keys():
            minpocz = min(niezbadane.values())
            for p in niezbadane.keys():
                if (niezbadane[p]==minpocz):
                    badany = p

            
            zbadane[badany] = niezbadane[badany]
            del niezbadane[badany]
            for i in niezbadane.keys():
                for j in range (0,self.iloscKrawedziR):
                    if(self.krawedzieR[j].poczatek == i or self.krawedzieR[j].poczatek == badany):
                        if(self.krawedzieR[j].koniec == i or self.krawedzieR[j].koniec == badany):
                            if(self.krawedzieR[j].waga + zbadane[badany] < niezbadane[i]):
                                niezbadane[i] = self.krawedzieR[j].waga + zbadane[badany]
                                kraNast[i-1] = badany
                              
      
        trasa = []
        trasa.append(kon)
        nast = kraNast[kon-1]
        while (nast!=pocz):
            trasa.append(nast)
            nast = kraNast[nast-1]

        trasa.append(pocz)
        cena =0
        for i in range(1,len(trasa)):
            for j in range(len(mozliwosc)):
                cena+= math.sqrt(pow(self.wierzcholkiR[trasa[i]-1].wspolrzedneX - self.wierzcholkiR[trasa[i-1]-1].wspolrzedneX,2) + pow(self.wierzcholkiR[trasa[i]-1].wspolrzedneY - self.wierzcholkiR[trasa[i-1]-1].wspolrzedneY,2))*(self.kableR[mozliwosc[j]-1].koszt)

        wspx = []
        wspy = []

        for i in range (0,len(trasa)):
            wspx.insert(i, self.wierzcholkiR[trasa[i]-1].wspolrzedneX)
            wspy.insert(i, self.wierzcholkiR[trasa[i]-1].wspolrzedneY)
        

        penS = len(mozliwosc)+10
        green=1.0
        penC = (0,green,0)

        for i in range(len(mozliwosc)):
            
            turtle.pensize(penS)
            turtle.pencolor(penC)
            for j in range (0,len(trasa)-1):
                turtle.pu()
                turtle.goto(wspx[j],wspy[j])
                turtle.pd()
                turtle.goto(wspx[j+1],wspy[j+1])
            penS-=3
            green-=0.2
            penC = (green,1,green)


        return cena

    def optymalizuj(self):
        
        klienci = []

        for i in range(self.iloscWierzcholkowR):
            if(self.wierzcholkiR[i].liczbaKlientow==-1):
                idCentrali = self.wierzcholkiR[i].id
            elif(self.wierzcholkiR[i].liczbaKlientow!=0):
                klienci.append(self.wierzcholkiR[i].id)

        #ustawianie id kabli pojemnosciami rosnaco#

        poKoleiPojemnosc = []
       
        tempKable = self.kableR[:]

        for j in range(self.iloscKabliR):
            tempNajwiekszaPojemnosc = tempKable[0].pojemnosc
            tempNajwiekszaPojemnoscId = tempKable[0].id
            for i in range(len(tempKable)):
                if(tempNajwiekszaPojemnosc>tempKable[i].pojemnosc):
                    tempNajwiekszaPojemnosc = tempKable[i].pojemnosc
                    tempNajwiekszaPojemnoscId = tempKable[i].id
                    
            poKoleiPojemnosc.append(tempNajwiekszaPojemnoscId)
            tempKable.remove(self.kableR[tempNajwiekszaPojemnoscId-1])

        #algorytm rozbijajacy ilosc klientow na rozne dobory dostepnych pojemnosci

        for iter in range(len(klienci)):
            mozliwosci = []
            tempIleKlientow = self.wierzcholkiR[klienci[iter]-1].liczbaKlientow
            tempMozliwosci = []

            while(tempIleKlientow>0):
                tempIleKlientow-=self.kableR[poKoleiPojemnosc[0]-1].pojemnosc
                tempMozliwosci.append(self.kableR[poKoleiPojemnosc[0]-1].id)
            mozliwosci.append(tempMozliwosci)
            totalyTemp = len(tempMozliwosci)
            for j in range(1,self.iloscKabliR):

               
                for i in range(1,totalyTemp):
                     
                    tempIleKlientow = self.wierzcholkiR[klienci[iter]-1].liczbaKlientow     
                    tempMozliwosci = []
                    tempSprawdzalnik = []
                    tempFlag=0
                    if(i*(self.kableR[j].pojemnosc)<=self.wierzcholkiR[klienci[iter]-1].liczbaKlientow):
                        for ii in range(i):
                            tempIleKlientow-=self.kableR[j].pojemnosc
                            tempMozliwosci.append(self.kableR[j].id)
                            tempPamiecIleKlientow = tempIleKlientow
                            tempPamiecMozliwosci = tempMozliwosci[:]
                        
                        jj=j
                        while(jj!=0):
                            for iii in range(int(tempIleKlientow/self.kableR[jj-1].pojemnosc)):
                                tempIleKlientow-=self.kableR[jj-1].pojemnosc
                                tempMozliwosci.append(self.kableR[jj-1].id)
                            jj-=1

                            if(tempIleKlientow==0 and tempMozliwosci and tempSprawdzalnik != tempMozliwosci):
                                tempSprawdzalnik = tempMozliwosci[:]
                                mozliwosci.append(tempMozliwosci)
                                tempMozliwosci = tempPamiecMozliwosci[:]
                                tempIleKlientow = tempPamiecIleKlientow
                                if(tempFlag==1):
                                    jj+=1
                            elif(tempIleKlientow!=0):
                                tempFlag=1
            
        #koniec najgorszego algorytmu świata        
            #
            
            najtanszaOpcja = 0

            for i in range(len(mozliwosci)):
                tempCena=0
                for j in range(len(mozliwosci[i])):
                    tempCena += self.kableR[mozliwosci[i][j]-1].koszt
                    
                if(najtanszaOpcja==0 or najtanszaOpcja>tempCena):
                    najtanszaOpcja = tempCena
                    najtanszaOpcjaID = i;
            
            
            cena = self.dijkstra(idCentrali,klienci[iter],mozliwosci[najtanszaOpcjaID])

            print("Klienci w Wierzcholku ",klienci[iter]," maja lacze poproawdzone z centrali", idCentrali," zgodnie z wykresem")
            print("Kosztuje ona ", cena)
            print("Uzyto nastepujacych typow kabli w nastepujacej ilosci",mozliwosci[najtanszaOpcjaID])
            input("Press Enter to continue...")
                
                

            



            



        


                
