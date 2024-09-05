# Python Moduuli- 5 Tehtävät (Listarakenne ja läpikäyvä toistorakenne (for)
# Tehtävä-1
import random

# Kysy käyttäjältä arpakuutioiden lukumäärä
n = int(input("Kuinka monta arpakuutiota haluat heittää? "))

# Muuttuja silmälukujen summan tallentamiseen
summa = 0

# Heitä arpakuutiota ja laske silmälukujen summa
for i in range(n):
    silmaluku = random.randint(1, 6)  # Satunnainen luku välillä 1-6
    summa += silmaluku

# Tulosta silmälukujen summa
print(f"Kaikkien arpakuutioiden silmälukujen summa on: {summa}")
