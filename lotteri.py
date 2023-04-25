import random

class Lotteri:
    def __init__(self):
        self.list_vinster = [
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "inget",
           "2080 Super"
           ]
    
    def get_vinst(self):
        slumptal = random.randint(0, 28)
        return self.list_vinster[slumptal]
    