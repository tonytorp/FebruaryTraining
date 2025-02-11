# Harjoitus 1
nimi = input("Anna nimesi: ")
ika = int(input("Anna ikäsi: "))
pituus = float(input("Anna pituutesi (metreina): "))

print(f"Hei {nimi}! Olet {ika} vuotias ja {pituus:.2f} metriä pitkä.")


# Harjoitus 2

# Graafisella käyttöliittymällä (TKinter, Pythonin sisään rakennettu)
import tkinter.simpledialog
import tkinter.messagebox

nimi = tkinter.simpledialog.askstring("Nimi", "Anna nimesi?")
ika = tkinter.simpledialog.askinteger("Ika", "Anna ikasi?")

tkinter.messagebox.showinfo("Omat tietosi", f"Hei {nimi} olet {ika} vuotta vanha.")

