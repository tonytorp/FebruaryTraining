from itertools import accumulate
nums = [1,2,3,4,5]
result = list(accumulate(nums))
print( result )

#Tehtävä 5B
from itertools import accumulate

paiva = input("Syota viikonpaiva: ").strip().lower()

match paiva:
    case "maanantai" | "tiistai" | "keskiviikko" | "torstai" | "perjantai":
        print( "arkipäivä")
    case "lauantai" | "sunnuntai":
        print( "viikonloppu" )
    case _:
        print("Tuntematon päivä")

#Tehtävä 6
# Tulostetaan luvut 1-100
for i in range(1,101):
    print(i)

# Tulostetaan lukujen 1-100 summa (# voi käyttää myös sum -funktiota iteraattorilla forin sijaan)
summa = 0
for i in range(1, 101):
    summa += i

print(f"Summa on {summa}")
summa = sum(range(1,101))

# Tulostetaan parittomat luvut (joka toinen luku)
for i in range(1, 101, 2):
    print( i )

# ostoslista list
ostoslista = []
while True:
    tuote = input("Syota tuote (q=quit):")
    if tuote == "q":
        break
    ostoslista.append( tuote )

print("Ostoslista:")
for tuote in ostoslista:
    print( " " + tuote )

# katsotaan, löytyykö banaani listalta
if "banaani" in ostoslista:
    print(f"Banaani on listalla indeksissä {ostoslista.index("banaani")}")


# ostoslista set
ostossetti = set()
while True:
    tuote = input("Syota tuote (q=quit):")
    if tuote == "q":
        break
    ostossetti.add(tuote)

print("Ostossetti:")
for tuote in ostossetti:
    print(" " + tuote)

# katsotaan, löytyykö banaani listalta
if "banaani" in ostossetti:
    print("Banaani on setissä")


my_numbers = [1, 2,3,4,4,6,6,7,8,9]
numbers_set = set( my_numbers )

big_list = list(range(1,10000000)) # haku O(n)
big_set = set(big_list)  # o(1)


