from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("kutsutaan kuorrutettua funktiota")
        print("Tai lokitetaan tms")
        result = func(*args, **kwargs)
        print("Kuorrutetusta funktiosta palataan...")
        return result
    return wrapper


@my_decorator
def do_something():
    print("Printing hello from my function...")

@my_decorator
def do_something_else( name ):
    print(f"Hello {name}")

do_something_else("Ossi")


do_something() # kutsutaan doSomethingia, joka on kuorrutettu

do_something()