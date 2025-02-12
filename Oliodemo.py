

class Person:
    def __init__(self, name="tuntematon", age=0, phone="xxx"):
        self.__name = name # _Person__name
        self.__age = age
        self.__phone = phone
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
        return self.__name

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            print("Ika ei positiivinen")

    # Computated property
    @property
    def birth_year(self):
        return 2025-self.__age


x = Person("Pekka", 20)
print(f"Henkilon nimi on {x.name}")
x.age = -2
print( f"Henkilon syntymavuosi on {x.birth_year}")

# Legacy getter ja setter
x.set_name("Kalle") # ei python -henkinen tapa asettaa
x.set_age(-5)  # ei python -henkinen tapa asettaa
print(f"Kallen nimi on {x.get_name()}")



x.name = "Jussi"
x.age = 10
print( x )


