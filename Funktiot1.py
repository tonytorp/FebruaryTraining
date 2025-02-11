# Funktiot ja globaali muuttuja
x = 10


def my_function():
    x = 20  # paikallinen muuttuja, joka peittää globaalin samannimisen
    print(x)  # tulostuu 20


def my_global_modifier_function():
    global x  # luodaan sisäinen viittaus globaaliin x:ään
    x = 20
    print(x)


my_function()
print(x)  # tulostaa 10
my_global_modifier_function()
print(x)  # tulostaa 20


# Funktioharjoitus 1
def tervehdi(nimi, kellonaika="päivä"):
    match kellonaika:
        case "aamu":
            tervehdys = "Hyvää huomenta"
        case "päivä":
            tervehdys = "Hyvää päivää"
        case "ilta":
            tervehdys = "Hyvää iltaa"
        case _:
            tervehdys = "Hei"

    print(f"{tervehdys}, {nimi}")


tervehdi("Ossi", "aamu")


# Tehtävä 2: yksinkertaistettu verolaskuri. Palauttaa 3 arvoa Tuplena
def laske_vero(ansiotulot, kuntavero=20.0):
    if ansiotulot <= 21200:
        vero = ansiotulot * 0.1264
    elif ansiotulot <= 31500:
        vero = 2679.68 + (ansiotulot - 21200) * 0.19
    elif ansiotulot <= 52100:
        vero = 4636.68 + (ansiotulot - 31500) * 0.3025
    elif ansiotulot <= 88200:
        vero = 10868.18 + (ansiotulot - 52100) * 0.34
    elif ansiotulot <= 150000:
        vero = 23142.18 + (ansiotulot - 88200) * 0.4175
    else:
        vero = 48943.68 + (ansiotulot - 150000) * 0.4425

    kuntaveron_maara = kuntavero * ansiotulot
    kokonaisvero = vero + kuntaveron_maara
    nettotulot = ansiotulot - kokonaisvero
    return nettotulot, vero, kuntaveron_maara


# testataan verolaskuria
x, y, z = laske_vero(100000)


def handle_person_data(**personData):
    for key, value in personData.items():
        print(f"{key} {value}")


handle_person_data(nimi="Tony", puhelin="0401234567")
