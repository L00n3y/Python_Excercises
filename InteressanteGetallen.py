"""
Naam:           Melvin Boers
Studentnummer:  S1104522
Specialisatie:  IFICT
"""

#Vraagt gebruiker om invoer testgevallen
Waarde1 = int(input("Vul het aantal test getallen in lager dan 50"))
Cijferlijst = []
Lijst = []
c = 0
a = 0

#zolang a niet gelijk is aan waarde1, voegt de invoer van de gebruiker aan Cijferlijst toe. en zet a op 1 enzovoort.
while a != Waarde1:
    Cijferlijst.append(int(input("Vul een getal in tussen 0 en 100")))
    a += 1


#een loop dat stopt tot het bij aantal nummers in Cijferlijst is. vervolgens zet getallen gelijk aan b. daarna zet reken gelijk aan getallen.
#de while not loop maakt een variable x aan van formaat int, vervolgens maken wij van getallen een string.
#en met de python functie sum tellen wij de x en getallen bij elkaar op, als dit gelijk is aan variable reken
#voert hij getallen + reken uit.
for b in Cijferlijst:
    getallen = b

    while not(sum([int(x) for x in str(getallen)]) == b):
        getallen += b

    Lijst.append(getallen)
    c += 1

for i in range(0, c):
    print(Lijst[i])

