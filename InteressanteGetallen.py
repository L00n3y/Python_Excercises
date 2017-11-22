"""
Naam:           Melvin Boers
Studentnummer:  S1104522
Specialisatie:  IFICT
"""

# vraagt de input aan de gebruiker hoeveel getallen hij wil als deze maar onder de 50 is
Waarde1 = int(input("Vul het aantal test getallen in lager dan 50"))
Cijferlijst = []

"""
De waarde wordt de lengte van de array
Hierdoor kun je de testgetallen invullen
"""

a = 0

while a != Waarde1:
    Cijferlijst.append(int(input("Vul een getal in tussen 0 en 100")))
    a += 1

#Haal de testgetallen door de functie

for b in Cijferlijst:
    getallen = b
    reken = getallen

    while not(sum([int(x) for x in str(getallen)]) == reken):
        getallen += reken

print(Cijferlijst[0])
print(getallen)

