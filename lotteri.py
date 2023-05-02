import random

class Lotteri:
    def __init__(self):
        self.list_vinster = [
           "25 Kr",
           "20 Kr",
           "AMD Ryzen 7 5600x",
           "Presentkort 100 kr på valfri butik",
           "Tvål",
           "10 Kr",
           "2080 Super"
           ]
    
    def get_vinst(self):
        slumptal = random.randint(0, 6)
        return self.list_vinster[slumptal]
    