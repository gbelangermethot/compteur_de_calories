class Repas:
    def __init__(self, ID, date, type_repas, items=None):
        self.ID = ID
        self.date = date
        self.type_repas = type_repas
        self.items = items if items is not None else []

    def calories_total(self):
        total = 0
        for item in self.items:
            total += item.calories()
        return total