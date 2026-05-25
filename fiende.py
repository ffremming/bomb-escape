from spiller_celle import Spiller

class Fiende:
    def __init__ (self,x,y,spiller):
        self.x = x
        self.y = y
        self.spiller = spiller
    
    def oppdater(self):
        spillerkoordinat = self.spiller.hent_posisjon_liste()

        forskjellx = self.x - spillerkoordinat[0]
        forskjelly = self.y - spillerkoordinat[1]

        if abs(forskjellx) <= abs(forskjelly):
            if forskjelly < 0:
                self.y += 1
            else:
                self.y -= 1

        else:
            if forskjellx < 0:
                self.x += 1
            else:
                self.x -= 1

    def hent_posisjon_liste(self):
        return [self.x,self.y]   
    

