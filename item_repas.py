class Item_repas:
    def __init__(self, ID, repas, aliment, poids):
        self.ID = ID
        self.repas = repas
        self.aliment = aliment
        self.poids = poids

    def calories(self):
        return self.aliment.calories_par_gram * self.poids