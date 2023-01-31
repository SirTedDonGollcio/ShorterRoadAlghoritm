class Wierzcholek:
    id = 0
    wspolrzedneX = 0
    wspolrzedneY = 0
    obowiazkowy = False
    liczbaKlientow = 0

    def __init__(self, id, wspolrzedneX,wspolrzedneY, liczbaKlientow):
        self.id = id
        self.wspolrzedneX = wspolrzedneX
        self.wspolrzedneY = wspolrzedneY
        self.liczbaKlientow = liczbaKlientow

        