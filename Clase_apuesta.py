class Apuesta:
    def __init__(self):
        self.fichas = 5

    def __repr__(self):
        return f"Apuesta {self.fichas} Fichas"
    
    def ponerFicha(self, cuantas=1): 
        self.fichas = self.fichas + cuantas 

    def tomarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError(f"No hay tantas fichas(quedan{self.fichas})")
        self.fichas = self.fichas - cuantas

    def tomarTodas(self):       
        return self.fichas
    
    def tieneFichas(self,cuantas=1):
        return self.fichas >= cuantas
    
    def estaVacio(self):
        return self.fichas == 0
    

        
    

    
    

