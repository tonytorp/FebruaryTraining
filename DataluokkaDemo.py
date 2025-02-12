from dataclasses import dataclass
import pickle

@dataclass(order=True, frozen=False)
class Person:
    name: str
    phone: str = ""
    age: int = 0

persons = [
    Person("Kalle", "joioijoijoi", 20),
    Person("Ville", "joioijoijoi", 30),
    Person("Pekka", "joioijoijoi", 15),
]

persons.sort()

x = Person("Ville")
y = Person("Ville")

if x == y:
    print("Samat")

for p in persons:
    print( p )

def writePersonsToFile():
    with open("persons.pkl", "wb") as file:
        pickle.dump( persons, file)

def loadPersonsFromFile():
    with open("persons.pkl", "rb") as file:
        global persons
        persons = pickle.load(file)

print( persons )