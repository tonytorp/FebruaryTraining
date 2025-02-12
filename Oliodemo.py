

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
    # getteri ja setteri nimelle (perinteinen)
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age


x = Person("Pekka", 20)
x.set_name("Kalle")
x.set_age(10)
print( x )


