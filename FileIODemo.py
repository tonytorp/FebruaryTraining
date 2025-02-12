with open("file.txt", "w", encoding="utf-8") as file:
    file.write("Hello\n")

with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

print("Tiedoston sisältö: ", content )