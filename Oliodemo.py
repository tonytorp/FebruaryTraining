
class Person:
    # henkilöiden lukumäärä muistissa
    _personCount = 0 # staattiset
    def __init__(self, name="tuntematon", age=0, phone="xxx"):
        self.__name = name # _Person__name
        self.__age = age
        self.__phone = phone

        Person._personCount += 1

    def __del__(self):
        # tämä tapahtuu kun viittausta olioon ei ole ja gc poistaa olion
        print(f"{self.__name} poistetaan muistista")
        Person._personCount -= 1

    def __eq__(self, other):
        if isinstance(other, Person):
            return self.__name == other.__name and self.__age == other.__age
        return False

    # Järjestys nimen perusteella (ns. oletusjärjestys)
    def __lt__(self, other):
        if isinstance(other, Person):
            return self.__name < other.__name
        return False

    def greet(self):

        print(f"Hei, olen {self.__name} ja olen {self.__age} vuotias")
    def birthday(self):
        self.__age += 1

    def __str__(self):
     return f"Olen: {self.__name}, Age:{self.__age} vuotias"
    # getteri ja setteri nimelle ja iälle (perinteinen)
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age >= 0:
            self.__age = age

    # moderni property -mekanismi decoratorilla
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.getter
    def name(self):
        print("lisäkuorrute getterille")
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            raise ValueError("Ikä ei voi olla < 0!")

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
         self.__phone = value

    # Computated property
    @property
    def birth_year(self):
        return 2025-self.__age

    @staticmethod
    def person_count():
        return Person._personCount

# periytyminen. Employee is-a Person
# Employeella on nimi, ikä, puhelinnumero etc, mutta
# lisäksi titteli ja palkka
class Employee(Person):
    def __init__(self, name="", age=0, phone="", title="", salary=0.0):
        super().__init__(name, age, phone)
        self.__title = title
        self.__salary = salary

    # ylikirjoita greet ja __str__
    def __str__(self):
        return super().__str__() + f"titteli: {self.__title}, palkka: {self.__salary}"


    # @property ja @salary.setter palkalle
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def greet(self):
        print(f"Employeen {self.name} tervehdys..")
        # override kantaluokan toteutus


# Luo lista henkilöitä, johon lisäät sekä Person että Employee -olioita
# Iteroi lista läpi ja kutsu jokaiselle greet() (dynaaminen sidonta)

puhelinluettelo = [
    Person( "Pekka", 20, "+3582222222"),
    Employee("Kalle", 35,"+358226872", "Developer", 5000 ),
    Person( "Ossi", 20, "+358223222"),
    Employee( "Maija", 30, "+22222999", "Project manager", 5000)
]
puhelinluettelo.sort()

print("Nimijärjestys")
for p in puhelinluettelo:
    print( p ) ## nimijärjestyksessä

# oletuslajittelu _lt_ n mukaan
puhelinluettelo.sort(key=lambda person : person.age)

print("Käänteinen ikäjärjestys")
for p in puhelinluettelo:
    print( p )



# Haetaan kaikki alle 30 vuotiaat
persons_under_30 = list(filter( lambda person: person.age < 25, puhelinluettelo))

# moderni syntaksi
persons_under_30_modern = [person for person in puhelinluettelo if person.age < 25]

for p in persons_under_30_modern:
    print(p)

def find_phone_number( name ):
    return next( (person.phone for person in puhelinluettelo if person.name == name), None)

print(f"Pekan puhelinnumero on {find_phone_number("Pekka")}")

x = Person("Jussi", 30)
y = Person("Jussi", 30)

if x == y: # __eq__
    print ("samat")
else:
    print ("erit")

if x < y: # __lt__
    print( "jussi aakkosissa ennen maijaa")










