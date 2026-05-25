from celle import Celle
from  spiller_celle import Spiller
import random
from fiende import Fiende


class Brett:
    def __init__ (self,x,y):
        
        self.y = y
        self.x = x
        self.rutenett = self.lag_lister()
        self.naboliste = self.hent_naboer()
        self.spiller = Spiller(15,10)
        self.fiende = Fiende(30,10,self.spiller)
        self.lag_hindringer()
        self.poeng = 0

    def lag_lister(self):
        nøstet_liste = []
        for y in range(self.y):
            lag_rad = []
            for x in range(self.x):
                celle = Celle(x,y) 
                #if y == self.y-1 or y == self.y-2:
                    #celle.gjør_hinder()
                if random.randint(0,12) == 0:
                    
                    celle.gjør_anker()
                else:
                    if random.randint(0,50) == 0:
                        celle.gjør_penge()
                

                    
                lag_rad.append(celle)
            nøstet_liste.append(lag_rad)

        return nøstet_liste

    def lag_hindringer(self):
        for y in self.rutenett:
            for x in y:
                
                if x.hent_anker():
                    
                    for nabo in x.hent_naboer():
                        if random.randint(0,10) == 2 and not nabo.er_penge():
                            nabo.gjør_grunn()
                            for innernabo in nabo.hent_naboer():
                                if random.randint(0,1) >= 0 and not nabo.er_penge():
                                    innernabo.gjør_hinder()
                                    for innernabo2 in nabo.hent_naboer() :
                                        if random.randint(0,1) <= 1 and not nabo.er_penge():
                                            innernabo2.gjør_hinder()
                                            
    def lag_hindringer2(self):         
        for y in self.rutenett:
            for x in y:
                
                if x.hent_anker():
                    
                    for nabo in x.hent_naboer():
                        if random.randint(0,5) == 2 and not nabo.er_penge():
                            

                            nabo.rekursiv_hinder(0)

                            """for innernabo in nabo.hent_naboer():
                                if random.randint(0,1) >= 0 and not nabo.er_penge():
                                    innernabo.gjør_hinder()
                                    for innernabo2 in nabo.hent_naboer() :
                                        if random.randint(0,1) <= 1 and not nabo.er_penge():
                                            innernabo2.gjør_hinder()"""

    def hent_naboer(self):
       
        for y in range(self.y):
            for x in range(self.x):
                self.koble_naboer(x,y)
                
    def koble_naboer(self,x,y):
        potensielle_naboer = []
        celle = self.hent_celle(x,y)
        for i in [1,-1]:
            potensielle_naboer.append(self.hent_celle(x+i,y))
            potensielle_naboer.append(self.hent_celle(x,y+i))
            potensielle_naboer.append(self.hent_celle(x+i,y+i))
            potensielle_naboer.append(self.hent_celle(x+i,y-i))

        for x in potensielle_naboer:
            if x!= None:
                celle.legg_til_nabo(x)


    def hent_celle(self,x,y):
        try:
            return self.rutenett[y][x]
        except:
            pass

    def tegn(self):
        print(self.poeng)
        for y in self.rutenett:
            for x in y:
                print(x.hent_tegn(self.spiller,self.fiende),end = " ")
            print("\n")

    def oppdater(self,retning):
                xy = self.spiller.hent_posisjon_liste()
                print("oppdatering")
                if retning == "opp" and not self.hent_celle(xy[0],xy[1]-1).er_hinder():# and not self.hent_celle(xy[0]+1,xy[1]).hent_grunn():
                    self.spiller.opp()
                    print("opp")
                elif retning == "ned" and not self.hent_celle(xy[0],xy[1]+1).er_hinder():# and not self.hent_celle(xy[0]+1,xy[1]).hent_grunn():
                    self.spiller.ned()
                    print("ned")
                elif retning == "hoyre" and not self.hent_celle(xy[0]+1,xy[1]).er_hinder():# and not self.hent_celle(xy[0]+1,xy[1]).hent_grunn():
                    self.spiller.høyre()
                    print("høyre")
                elif retning == "venstre" and not self.hent_celle(xy[0]-1,xy[1]).er_hinder():# and not self.hent_celle(xy[0]+1,xy[1]).hent_grunn():
                    self.spiller.venstre()
                    print("høyre")
    def kast_granat(self,retning):
        xy = self.spiller.hent_posisjon_liste()

        if retning == "opp" :

            for x in (self.hent_celle(xy[0],xy[1]-3)).hent_naboer():
                x.fjern_hinder()
                (self.hent_celle(xy[0],xy[1]-3)).fjern_hinder()


        elif retning == "ned" :
            for x in (self.hent_celle(xy[0],xy[1]+3)).hent_naboer():
                x.fjern_hinder()
                (self.hent_celle(xy[0],xy[1]+3)).fjern_hinder()

        elif retning == "hoyre" :
            for x in (self.hent_celle(xy[0]+3,xy[1])).hent_naboer():
                x.fjern_hinder()
                (self.hent_celle(xy[0]+3,xy[1])).fjern_hinder()

        elif retning == "venstre":
            for x in (self.hent_celle(xy[0]-3,xy[1])).hent_naboer():
                x.fjern_hinder()
                (self.hent_celle(xy[0]-3,xy[1])).fjern_hinder()

    def bombe(self):
        xy = self.spiller.hent_posisjon_liste()
        for x in (self.hent_celle(xy[0],xy[1])).hent_naboer():
            x.fjern_hinder()
            for i in x.hent_naboer():
                    i.fjern_hinder()

    def hent_fiende(self):
        return self.fiende

    def hent_spiller(self):
        return self.spiller

    def sjekk_penge(self):
        for y in self.rutenett:
            for x in y:
                if x.er_penge():
                    if x.hent_posisjon()== (self.hent_spiller()).hent_posisjon_liste():
                        self.poeng += 1
                        x.fjern_penge()


b = Brett(40,15)
print(b.hent_celle(4,4).hent_naboer())


retning = "opp"
avslutt = False
while avslutt == False:
    b.tegn()
    inp = input("o/n/h/v, b/g , enter")
    if inp == "o":
        retning = "opp"
    elif inp == "n":
        retning = "ned"
    elif inp == "h":
        retning = "hoyre"
    elif inp == "v":
        retning = "venstre"
    
    elif inp == "g":
        b.kast_granat(retning)

    elif inp == "b":
        b.bombe()

    elif inp == "":
        b.oppdater(retning)
    if random.randint(0,3) < 2:
        (b.hent_fiende()).oppdater()

    if b.hent_fiende().hent_posisjon_liste() == (b.hent_spiller()).hent_posisjon_liste():
        avslutt = True
    b.sjekk_penge()

    
    


