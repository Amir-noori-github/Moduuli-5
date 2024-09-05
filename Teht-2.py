# Python Moduuli-5, Tehtävä 2

# Lista käyttäjän syöttämien lukujen tallentamiseen
luvut = []

# Kysytään lukuja käyttäjältä, kunnes tyhjä syöte annetaan
while True:
    syote = input("Anna luku (tyhjä syöte lopettaa): ")

    # Tarkistetaan, onko syöte tyhjä
    if syote == "":
        break

    # Muutetaan syöte luvuksi ja lisätään listaan
    try:
        luku = int(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötä kelvollinen numero.")

# Lajitellaan luvut suurimmasta pienimpään
luvut.sort(reverse=True)

# Tulostetaan viisi suurinta lukua
print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)
