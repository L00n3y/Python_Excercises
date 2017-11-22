"""
Berekent de 4 meest voorkomende woorden in de dictionary, in dit geval uit words.
"""
from collections import Counter

words = ['hi', 'bye', 'good', 'morning', 'hi', 'bye', 'pink', 'purple', 'dead', 'hi', 'dead', 'pink', 'red', 'GOT', 'GOT', 'Walking dead', 'carpet', 'Bye', 'Good', 'Morning']

AantalWoorden = Counter(words)
topVier = AantalWoorden.most_common(4)

print(topVier)