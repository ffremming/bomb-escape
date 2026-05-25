class Spiller:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def opp(self):
        self.y -= 1
    
    def ned(self):
        self.y += 1

    def høyre (self):
        self.x += 1

    def venstre (self):
        self.x -= 1
        print("vesntre")

    def hent_posisjon_liste(self):
        return [self.x,self.y]

    
