class pizzas:
    def __init__(self, naam, grootte, ingrediënten, prijs):
        self.naam = naam
        self.grootte = grootte
        self.ingrediënten = ingrediënten
        self.prijs = self.bereken_prijs

    def print_naam_en_grootte(self):
        print(f"De " + self.naam + " is " + self.grootte + "cm" + " groot.")
    def toon_informatie(self):
        print(f"De ingrediënten van de {self.naam} zijn: {self.ingrediënten}")
        print("Prijs is: " + self.prijs)
    def bepaal_prijs(self):
        basisprijs = 0.0
        if self.grootte == 16:
            basisprijs = 8.99
        elif self.grootte == 22:
            basisprijs = 10.99
        elif self.grootte == 28:
            basisprijs = 12.99
        basisprijs += len(self.ingrediënten) * 1.5
        return basisprijs



pizza_margharitta = pizzas("pizza margharitta", "22",["bladerdeeg", "kruiden", "tomatensaus" , "kaas"], 10.99)
pizza_champiljong = pizzas("pizza champiljong", "16", ["bladerdeeg", "kruiden", "tomatensaus", "kaas", "champiljongen"], 8.99)
pizza_pepperoni = pizzas("pizza pepperoni", "28", ["bladerdeeg", "kruiden", "tomatensaus", "kaas", "pepperoni"], 12.99)
pizza_margharitta.print_naam_en_grootte()
pizza_champiljong.print_naam_en_grootte()
pizza_pepperoni.print_naam_en_grootte()
pizza_margharitta.toon_informatie()
pizza_champiljong.toon_informatie()
pizza_pepperoni.toon_informatie()
print(f'prijs: {pizza_margharitta.bepaal_prijs()}')
print(f'prijs: {pizza_champiljong.bepaal_prijs()}')
print(f'prijs: {pizza_pepperoni.bepaal_prijs()}')