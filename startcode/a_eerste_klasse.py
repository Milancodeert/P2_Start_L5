
class Dier:
    def __init__(self, naam, geluid):
        self.naam = naam
        self.geluid = geluid

    def maak_geluid(self):
        print(f"De {self.naam} zegt '{self.geluid}'.")
koe = Dier("koe", "boe")
hond = Dier("hond", "waf")
kat = Dier("kat", "miauw")
kat.maak_geluid()
hond.maak_geluid()
koe.maak_geluid()