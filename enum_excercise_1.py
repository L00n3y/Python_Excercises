from enum import Enum

#class Country aanmaken met de python functie Enum. Deze functie zorgt ervoor dat er een member en een value is.
#Door deze member en value kan gerouteerd worden.
class Country(Enum):
    StarWars = 10
    LOTR = 100
    GOT = 1000
    Walking_Dead = 1250

#Nu roepen wij een member en de value aan.
print('\nMember name: {}'.format(Country.GOT.name))
print('Member value: {}'.format(Country.GOT.value))