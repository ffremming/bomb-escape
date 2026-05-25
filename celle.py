from  spiller_celle import Spiller
import colorama
from colorama import Fore,Back,Style
from random import randint
class Celle:
    def __init__(self,x,y):
        self.x = x
        self.y = y  
        self.hinder = False
        self.naboer = []
        self.anker = False
        self.grunn = False
        self.penge = False
        


    def fjern_hinder(self):
        if self.grunn == False:
            self.hinder = False

    def er_hinder(self):
        return self.hinder

    def gjør_anker(self):
        self.anker = True
        self.hinder = False
        self.grunn = True
    def hent_anker(self):
        return self.anker

    def gjør_hinder(self):
        self.hinder = True

    def rekursiv_hinder(self,antall):
        
            self.hinder = True  
            antall += 1
            if antall < 3:
                try:
                    (self.naboer[randint(0,7)]).rekursiv_hinder(antall)
                except:
                    self.naboer[2].rekursiv_hinder(antall)

    def gjør_grunn(self):
        self.grunn = True
        self.hinder = True
    def hent_grunn(self):
        print(self.grunn)

        return self.grunn
        
    def er_penge(self):
        return self.penge

    def gjør_penge(self):
        self.penge = True
        self.grunn = False  
        self.hinder = False

    def fjern_penge(self):
        self.penge = False

    def hent_tegn(self,spiller,fiende):
        
        if self.er_penge():
            
            return f"{Fore.YELLOW}0{Style.RESET_ALL}"
        if self.hent_posisjon()== spiller.hent_posisjon_liste():
            return f"{Fore.GREEN}O{Style.RESET_ALL}"
        if self.hent_posisjon()== fiende.hent_posisjon_liste():
            return f"{Fore.RED}§{Style.RESET_ALL}"
        if self.grunn:
            return f"{Back.WHITE}#{Style.RESET_ALL}"
        if self.hinder:
            return f"{Back.WHITE}¤{Style.RESET_ALL}"
        else:
            return "."

    def legg_til_nabo(self,nabo):
        self.naboer.append(nabo)
    
    def hent_naboer(self):
        return self.naboer
                

    def __str__(self):
        return f"({self.y})"

    def hent_posisjon(self):
        return [self.x,self.y]