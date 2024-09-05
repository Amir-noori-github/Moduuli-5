# Python Moduuli-5, Tehtävä 3

# Funktio, joka tarkistaa, onko luku alkuluku
def onko_alkuluku(luku):
    # Alkuluvut ovat suurempia kuin 1
    if luku < 2:
        return False

    # Tarkistetaan, onko luku jaollinen jollakin muulla kuin ykkösellä ja itsellään
    for i in range(2, int(luku ** 0.5) + 1):  # Tarkistetaan luvut 2 - sqrt(luku)
        if luku % i == 0:
            return False

    return True

# Kysytään käyttäjältä kokonaisluku
luku = int(input("Anna kokonaisluku: "))

# Tarkistetaan, onko luku alkuluku ja tulostetaan tulos
if onko_alkuluku(luku):
    print(f"{luku} on alkuluku.")
else:
    print(f"{luku} ei ole alkuluku.")
