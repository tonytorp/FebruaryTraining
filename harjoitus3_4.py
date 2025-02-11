#Harjoitus 3
perushinta = 15.00
ika = int( input("Anna ikasi: "))
# strip poistaa ylimääräiset välilyönnit (tabit ja rivinvaihdot) merkkijonon päistä ja lower muuttaa syötteen lower caseksi
opiskelija = input("Oletko opiskelija (k/e)").strip().lower() == "k"

if ika < 5:
    hinta = 0
elif 5 <= ika <= 17:
    hinta = perushinta * 0.7
elif ika >= 65 or opiskelija:
    hinta = perushinta * 0.8
else:
    hinta = perushinta

print(f"Lipun hinta on {round(hinta,2)}€")

#Harjoitus 4
# poistetaan käyttäjätunnuksesta turhat välilyönnit ja muuttaa pieniksi kirjaimiksi
kayttajatunnus = input("Luo kayttajatunnus: ").strip().lower()
salasana = input("Luo salasana: ")

# Salasanassa tulee olla vähintään 8 kirjainta, ei koostu pelkistä kirjaimista, vähintään 1 numero
on_numero = False
on_kirjain = False
pituus = len(salasana)


for i in range(pituus):
    if salasana[i].isdigit():
        on_numero = True

on_numero = any( merkki.isdigit() for merkki in salasana )

if on_numero and pituus >= 8:
    print("Salasana on laillinen")

numerot = [ 1, -2, 3, 4, 5, 6]
has_negative_number = any( n < 0 for n in numerot)




