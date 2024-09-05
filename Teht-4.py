# Python Moduuli-5, Tehtävä 4

# Lista kaupunkien nimien tallentamiseen
kaupungit = []

# Kysy kaupungin nimiä käyttäjältä for-toistorakenteella
for i in range(5):
    kaupunki = input(f"Anna kaupungin nimi {i+1}: ")
    kaupungit.append(kaupunki)

# Tulosta kaupunkien nimet yksi kerrallaan for/in-toistorakenteella
print("Kaupungit, jotka annoit:")
for kaupunki in kaupungit:
    print(kaupunki)
